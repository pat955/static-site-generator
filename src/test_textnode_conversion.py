import unittest

from main import text_node_to_html_node, extract_markdown_images, extract_markdown_links
from textnode import TextNode

class TestParentNode(unittest.TestCase):
    def test_to_htmlnode(self):
        node = TextNode("Hello", "bold")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>Hello</b>")
    
    def test_to_htmlnode2(self):
        node = TextNode("I loved strawberries", "italic")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<i>I loved strawberries</i>")

    def test_to_htmlnode3(self):
        node = TextNode("This is", "image", "https://example.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<img src=\"https://example.com\" alt=\"This is\"></img>")
        
    def split_images(self):
        text = "text test text test image here soon!! ![nope] here: ![image](https://example.png)"
        res = extract_markdown_images(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("image", "image", "https://example.png"),]

        self.assertEqual(res, answer)
    
    def split_images2(self):
        print("testing...")
        text = "text test text test image here soon!! ![nope] here: ![image](https://example.png)  !!!! second image???? ![2](https://hello.png)"
        res = extract_markdown_images(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("image", "image", "https://example.png"),
        TextNode("  !!!! second image???? ", "text"),
        TextNode("2", "image", "https://hello.png")
        ]
        self.assertEqual(res, answer)
    
    def split_links(self):
        text = "text test text test image here soon!! ![nope] here: [link!](https://example.png)  !!!! second image???? ![2](https://hello.png)"
        res = extract_markdown_links(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("link!", "link", "https://example.png"),
        TextNode("  !!!! second image???? ", "text"),
        TextNode("2", "image", "https://hello.png")
        ]
        self.assertEqual(res, answer)
# "<img>src=\"https://example.com\" alt=\"I loved This is an image of a capibarra\"</img>"
# 
