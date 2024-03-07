import unittest

from htmlnode import LeafNode

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
    

