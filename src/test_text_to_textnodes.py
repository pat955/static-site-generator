import unittest
from split_nodes import text_to_textnodes
from textnode import TextNode

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