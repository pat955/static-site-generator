import re 
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

# TODO
# Remove empty blocks?

def markdown_to_blocks(markdown):
    return re.split(r"\n\n", markdown)
    

def block_to_block_type(markdown):
    if re.match(r"[#]{1,6}[ ]", markdown):
        return "heading"
    
    elif re.match(r"```[\S|\s]*?```", markdown):
        return "code"
    
    quote = True
    ordered = True
    unordered = True
    
    i = 0
    for line in markdown.split("\n"):
        line = line.strip()
        if line == "":
            continue

        i += 1
        if line[0] != ">":
            quote = False
        
        if line[0] != "*" and line[0] != "-":
            unordered = False
        
        if not line.startswith(f"{i}."):
            ordered = False

    if quote:
        return "quote"
    elif unordered:
        return "unordered"
    elif ordered:
        return "ordered"
    return "paragraph"


def list_block(parent_node, block, block_type):
    # Add correct list type to parent node. 
    if block_type == "ordered":
        list_node = ParentNode("ol", children=[])
    else:
        list_node = ParentNode("ul", children=[])

    for line in block.split("\n"):
        if line == "":
            continue
        list_node.children.append(LeafNode(tag="li", value=re.sub(r"^- |\d. ", "", line)))
    parent_node.children.append(list_node)


def quote_block(parent_node, block):
    # Replaces the quote signs and adds a quote block to parent node
    block = block.replace("> ", "")
    quote_node = LeafNode(tag="blockquote", value=block.replace("> ", ""))
    parent_node.children.append(quote_node)


def code_block(parent_node, block):
    # Container node has tag pre for preformatted text element. 
    # With regex extracts the code and removes ```
    container_node = ParentNode(tag="pre", children=[])
    container_node.children.append(LeafNode(tag="code", value=re.findall(r"```\n([\S\s]*?)```", block)[0]))
    parent_node.children.append(container_node)


def heading_block(parent_node, block):
    i = len(re.search(r"([#]{1,6})[ ]", block)[0]) - 1
    parent_node.children.append(LeafNode(tag=f"h{i}", value=block.strip("\n")[i+1:]))

### ^ Blocks
### v Nodes 

def markdown_to_html_node(markdown):
    # Make top level node that we will later push into {{ Content }} in template html.
    # Get each blocks type and convert them to textnodes, then convert textnodes into html and add to hmtl block.
    # Sorts through each block type and add itself and potential child nodes to toplevel.
    toplevel_node = ParentNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        text_nodes = text_to_textnodes(block)
        html_block = ""

        for text_node in text_nodes:
            html_block += text_node_to_html_node(text_node).to_html()

        if block_type == "heading":
            heading_block(toplevel_node, html_block)

        elif block_type == "quote":
            quote_block(toplevel_node, html_block)

        elif block_type in ["unordered", "ordered"]:
            list_block(toplevel_node, html_block, block_type)

        elif block_type == "code":
            code_block(toplevel_node, html_block)
        
        else:
            toplevel_node.children.append(LeafNode(tag="p", value=html_block))
    return toplevel_node


def text_to_textnodes(text):
    # For each basic delimiter calls split_nodes_delimiter. 
    # Then the more difficult splits like code and links are called.
    # Returns a list of all the new nodes separated into types.
    del_dict = {
        "bold" : "**",
        "italic" : "*"
    }

    new_nodes = [TextNode(text, "text")]
    
    for name, delim in del_dict.items():
        new_nodes = split_nodes_delimiter(new_nodes, delim, name)

    new_nodes = split_nodes_code(new_nodes)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
   
    return new_nodes


def text_node_to_html_node(node):
    types_dict = {
        # name : (params: tag, text, props) 
        "bold" : ("b", node.text),
        "italic" : ("i", node.text),
        "code" : ("code", node.text),
        "link" : ("a", node.text, {"href": node.url}),
        "image" : ("img", "", {"src": node.url, "alt": node.text})
    }
    if node.text_type == "text":
        return LeafNode(value=node.text)
        
    for typ, params in types_dict.items():
        if node.text_type == typ:
            return LeafNode(*params)
    raise Exception("Not A Supported Type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    del_count = len(delimiter)
    for node in old_nodes:
        if type(node) != TextNode or node.text_type != "text":
            new_nodes.append(node)
            continue

        split_nodes = re.split(f"[{delimiter}]{{{del_count}}}([^{delimiter}]*?)[{delimiter}]{{{del_count}}}", node.text)
        matches = re.findall(f"[{delimiter}]{{{del_count}}}([^{delimiter}]*?)[{delimiter}]{{{del_count}}}", node.text)
        
        for text in split_nodes:
            if text in matches:
                new_nodes.append(TextNode(text, text_type))
                continue
            new_nodes.append(TextNode(text, "text"))
    return new_nodes


def split_nodes_code(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        temp_merged_str = ""
        if node.text == None:
            continue

        code = re.findall(r"[^`](`[^`]*?`)[^`]", node.text)
        if not code:
            new_nodes.append(node)
            continue
        
        split =  re.split(r"(`[^`]+`)", node.text)
        line_pos = -1

        for new_node in split:
    
            line_pos += 1
            if new_node == "":
                continue
            
            if new_node in code:
                if split[line_pos - 1][-1] == "`" and line_pos != 0:
                    temp_merged_str += new_node
                    print(new_node, "continued...")
                    continue

                if temp_merged_str != "":
                    new_nodes.append(TextNode(temp_merged_str, "text"))
                    temp_merged_str = ""

                new_nodes.append(TextNode(new_node.strip("`"), "code"))
            else:
                temp_merged_str += new_node

        if temp_merged_str != "":
            new_nodes.append(TextNode(temp_merged_str, "text"))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^]]*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"[^!]\[([^]]*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        temp_merged_str = ""
        
        if node.text == None:
            continue

        images = extract_markdown_images(node.text)
        
        if not images:
            new_nodes.append(node)
            continue
        
        split = re.split(r"(!\[[^]]*?\]\(.*?\))", node.text)

        for new_node in split:
            if new_node == "":
                continue

            try:
                image_tuple = re.findall(r"!\[([^]]*?)\]\((.*?)\)", new_node)[0]
                
            except Exception as e:
                image_tuple = []

            if image_tuple in images:
                if temp_merged_str != "":
                    new_nodes.append(TextNode(temp_merged_str, "text"))
                    temp_merged_str = ""

                new_nodes.append(TextNode(image_tuple[0], "image", image_tuple[1]))
        
            else:
                temp_merged_str += new_node

        if temp_merged_str != "":
            new_nodes.append(TextNode(temp_merged_str, "text"))
    
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        temp_merged_str = ""
        if node.text == None:
            continue

        links = re.findall(r"[^!]\[([^]]*?)\]\((.*?)\)", node.text)
        
        if not links:
            new_nodes.append(node)
            continue
        
        split =  re.split(r"(\[[^]]*?\]\(.*?\))", node.text)
        
        for new_node in split:
            if new_node == "":
                continue
            try:
                link_tuple = re.findall(r"\[([^]]*?)\]\((.*?)\)", new_node)[0]
                
            except Exception as e:
                link_tuple = []

            if link_tuple in links:
                if temp_merged_str != "":
                    new_nodes.append(TextNode(temp_merged_str, "text"))
                    temp_merged_str = ""

                new_nodes.append(TextNode(link_tuple[0], "link", link_tuple[1]))
            else:
                temp_merged_str += new_node

        if temp_merged_str != "":
            new_nodes.append(TextNode(temp_merged_str, "text"))
    return new_nodes