import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test1(self):
        node = ParentNode("head", [LeafNode("b", "Bold text"), 
        ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),])])
        self.assertEqual(node.to_html(), "<head><b>Bold text</b><p><b>Bold text</b>Normal text<i>italic text</i></p></head>")