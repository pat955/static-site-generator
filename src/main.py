
import re
from textnode import TextNode
from htmlnode import LeafNode

def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    print(new_nodes)
    # text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)! !!!!"

    # print(extract_markdown_images(text))
    # text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text))


def text_node_to_html_node(node):
    types = ["text", "bold", "italic", "code", "link","image"]
    if node.text_type not in types:
        raise Exception("Not A Supported Type")

    if node.text_type == "text":
        return LeafNode(value=text_node.text)

    elif node.text_type == "bold":
        return LeafNode("b", node.text)

    elif node.text_type == "italic":
        return LeafNode("i", node.text)
    
    elif node.text_type == "code":
        return LeafNode("code", node.text)

    elif node.text_type == "link":
        return LeafNode("a", node.text, {"href": node.url})
    
    elif node.text_type == "image":
        return LeafNode("img", "", {"src": node.url, "alt": node.text})


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if type(node) != TextNode:
            new_nodes.append(node)
                  
        split_nodes = node.text.split(delimiter)
        matches = re.findall(f"[{delimiter}]+(.*?)[{delimiter}]+", node.text)

        for text in split_nodes:
            print(text in matches)
            if text in matches:
                new_nodes.append(TextNode(text, text_type))
                continue
            new_nodes.append(TextNode(text, "text"))

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)



main()