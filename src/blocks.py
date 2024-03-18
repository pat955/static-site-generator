import re 
from htmlnode import HTMLNode
def markdown_to_blocks(markdown):
    #remove trailing whitespace and empty blocks
    blocks = []
    start_of_block = 0 
    i = 0 
    
    split_markdown = [e.strip()+"\n" for e in markdown.split("\n")]
    split_markdown[-1] = split_markdown[-1][0:-1]
    
    for line in split_markdown:
        if line == "\n":
            blocks.append(''.join(split_markdown[start_of_block:i]))
            start_of_block = i + 1
        i += 1
    blocks.append(''.join(split_markdown[start_of_block:i]))
    return blocks

def block_to_block_type(markdown):

    if re.match(r"[#]{1,6}[ ]", markdown):
        return "heading"

    elif re.match("/{3}.*?/{3}", markdown):
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
    else:
        return "paragraph"

def markdown_to_html_node(markdown):
    toplevel_node = HTMLNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            heading_block(toplevel_node, block)

        elif block_type == "quote":
            quote_block(toplevel_node, block)

        elif block_type in ["unordered", "ordered"]:
            list_block(toplevel_node, block, block_type)

        elif block_type == "code":
            code_block(toplevel_node, block)
        
        else:
            toplevel_node.children.append(LeafNode(tag="p", value=block))
    return toplevel_node
    
    
def quote_block(parent_node, block):
    quote_node = LeafNode(tag="quoteblock", value=block)
    parent_node.children.append(quote_block)


def list_block(parent_node, block, block_type):
    if block_type == "ordered":
        list_node = HTMLNode("ol", children=[])
    else:
        list_node = HTMLNode("ul", children=[])

    for line in block.split("\n"):
        if line == "":
            continue
        list_node.children.append(LeafNode(tag="li", value=line))
    parent_node.children.append(list_node)


def code_block(parent_node, block):
    container_node = HTMLNode(tag="pre", children=[])
    container_node.children.append(LeafNode(tag="code", value=re.findall("[/]{3}(.*?)[/]{3}", block)[0]))
    parent_node.children.append(container_node)


def heading_block(parent_node, block):
    i = len(re.search(r"([#]{1,6})[ ]", block)[0]) - 1
    parent_node.children.append(LeafNode(tag=f"h{i}", value=block.strip("\n")[i+1:]))

    

