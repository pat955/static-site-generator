import unittest
from blocks import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode

class TestMarkdownToHTMLNodes(unittest.TestCase):
    pass
    # def test1(self):
    #     markdown = "*This is a\n*list\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n### This is a list\n\n///with items///"
    #     res = markdown_to_html_node(markdown)
    #     ans = HTMLNode(tag="div", children=[
    #         HTMLNode(tag="ul", children=[LeafNode(tag="li", value="*This is a"), LeafNode(tag="li", value="*list")]),
    #         LeafNode(tag="p", value="This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n"),
    #         LeafNode(tag="h3", value="This is a list"),
    #         HTMLNode(tag="pre", children=[LeafNode(tag="code", value="with items")])          
    #             ])
    #     self.assertEqual(res, ans)

    # def test2(self):
    #     markdown = "///code///\n\nparagraph...."
    #     res = markdown_to_html_node(markdown)
    #     ans = HTMLNode(tag="div", children=[HTMLNode(tag="pre", children=[LeafNode(tag="code", value="code")]), LeafNode(tag="p", value="paragraph....")])
    #     res.children = []
    #     ans.children = []
    #     print(res, "\n\n\n", ans, HTMLNode()==HTMLNode())
    #     self.assertEqual(res, ans)
    
    # def test3(self):
    #     markdown = "###### heading1 \n\n## heading2"
    #     res = markdown_to_html_node(markdown)
    #     ans = HTMLNode(tag="div", children=[LeafNode(tag="h6", value="heading1"), LeafNode(tag="h2", value="heading2")])
    #     self.assertEqual(res, ans)