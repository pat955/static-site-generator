
import re
import os 
import shutil
from textnode import TextNode
from htmlnode import LeafNode, HTMLNode
from split_nodes import *
from pages import generate_page

def main():
    copy_static()
    generate_page("./content/index.md", "./template.html", "./public/index.html")


def copy_static():
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")
    r_copy_static("./static", "./public")


def r_copy_static(p, destination):
    static_files = os.listdir(p)
    for file in static_files:
        print(f'Moving "{file}"...')
        if "." in file:
            shutil.copy(f"{p}/{file}", destination)
            
        else:
            os.mkdir(f"{destination}/{file}/")
            r_copy_static(f"{p}/{file}/", f"{destination}/{file}/")


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
        return LeafNode(value=text_node.text)
        
    for typ, params in types_dict.items():
        if node.text_type == typ:
            return LeafNode(*params)
    raise Exception("Not A Supported Type")

def text_to_textnodes(text):
    del_dict = {
        "bold" : "**",
        "italic" : "*",
        "code" : "`"
    }

    new_nodes = [TextNode(text, "text")]
    
    for name, delim in del_dict.items():

        new_nodes = split_nodes_delimiter(new_nodes, delim, name)

    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_links(new_nodes)
   
    return new_nodes

main()