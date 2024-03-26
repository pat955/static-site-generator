import unittest
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test2(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test3(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic", "idislikepaprika.com")
        self.assertNotEqual(node, node2)

    def test4(self):
        node = TextNode("This text node", "italic", "helloworld.com")
        node2 = TextNode("This is a text node", "italic", "helloworld.com")
        self.assertNotEqual(node, node2)
    
    def test5(self):
        node = TextNode("This is a text node", "italic", "helloworld.com")
        node2 = TextNode("This is a text node", "italic", "helloworld.com")
        self.assertEqual(node, node2)


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html3(self):
        node = LeafNode(value="NO TAGS!")
        self.assertEqual(node.to_html(), 'NO TAGS!')

    def test_to_html4(self):
        node = LeafNode("p")
        self.assertRaises(ValueError)


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


class TestTextToTextnodes(unittest.TestCase):
    def test1(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        res = text_to_textnodes(text)
        answer = [
        TextNode("This is ", "text"),
        TextNode("text", "bold"),
        TextNode(" with an ", "text"),
        TextNode("italic", "italic"),
        TextNode(" word and a ", "text"),
        TextNode("code block", "code"),
        TextNode(" and an ", "text"),
        TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and a ", "text"),
        TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(res, answer)