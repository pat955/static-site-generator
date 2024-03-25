import unittest
from blocks import split_nodes_code
from textnode import TextNode

class TestCodeSplit(unittest.TestCase):
    def test1(self):
        nodes = [TextNode("test", "text"), TextNode('we `coding` here', "text")]
        res = split_nodes_code(nodes)
        answer = [
        TextNode("test", "text"),
        TextNode("we ", "text"),
        TextNode("coding", "code"),
        TextNode(" here", "text")
        ]
        self.assertEqual(res, answer)