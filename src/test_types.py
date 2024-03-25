import unittest
from textnode import TextNode
from blocks import block_to_block_type, text_to_textnodes, markdown_to_blocks

class TestBlockTypes(unittest.TestCase):
    def test1(self):
        markdown = "## heading"
        res = block_to_block_type(markdown)
        ans = "heading"
        self.assertEqual(res, ans)
    
    def test2(self):
        markdown = "* unordered 1\n* 2\n* 3"
        res = block_to_block_type(markdown)
        ans = "unordered"
        self.assertEqual(res, ans)

    def test3(self):
        markdown = "```?code```\n"
        res = block_to_block_type(markdown)
        ans = "code"
        self.assertEqual(res, ans)
    
    def test4(self):
        markdown = "texttesttxtetxtfhdksjfkdflsjfkldsjfl\netsfodusofdofsudifusoifudsoesfdfksjflkds\n esfsdfd"
        res = block_to_block_type(markdown)
        ans = "paragraph"
        self.assertEqual(res, ans)


class TestMarkdownToBlocks(unittest.TestCase):
    def test1(self): 
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        res = markdown_to_blocks(markdown)
        ans = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        self.assertEqual(res, ans)
    
    def test2(self):
        markdown = "heading\n\npara\npara2\npara3\npara4\n\nsomething\nsomething\n\n"
        res = markdown_to_blocks(markdown)
        ans = ["heading", "para\npara2\npara3\npara4", "something\nsomething", ""]
        self.assertEqual(res, ans)

    def test3(self):
        markdown = "  something   \n"
        res = markdown_to_blocks(markdown)
        ans = ["something"]
        self.assertEqual(res, ans)


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