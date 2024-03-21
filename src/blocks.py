import re 
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode
from split_nodes import *

def markdown_to_blocks(markdown):
    # remove empty blocks
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
    else:
        return "paragraph"


def list_block(parent_node, block, block_type):
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
    block = block.replace("> ", "")
    quote_node = LeafNode(tag="blockquote", value=block)
    parent_node.children.append(quote_node)


def code_block(parent_node, block):
    container_node = ParentNode(tag="pre", children=[])
    container_node.children.append(LeafNode(tag="code", value=re.findall(r"```\n([\S\s]*?)```", block)[0]))
    parent_node.children.append(container_node)


def heading_block(parent_node, block):
    i = len(re.search(r"([#]{1,6})[ ]", block)[0]) - 1
    parent_node.children.append(LeafNode(tag=f"h{i}", value=block.strip("\n")[i+1:]))


def markdown_to_html_node(markdown):
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

def text_to_textnodes(text):
    del_dict = {
        "bold" : "**",
        "italic" : "*",
        "code" : "```"
    }

    new_nodes = [TextNode(text, "text")]
    
    for name, delim in del_dict.items():
        new_nodes = split_nodes_delimiter(new_nodes, delim, name)

    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
   
    return new_nodes