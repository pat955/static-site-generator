import unittest
from textnode import TextNode

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