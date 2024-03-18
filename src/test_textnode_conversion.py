import unittest

from main import text_node_to_html_node
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


# "<img>src=\"https://example.com\" alt=\"I loved This is an image of a capibarra\"</img>"
# 
