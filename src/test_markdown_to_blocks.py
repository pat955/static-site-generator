import unittest
from blocks import markdown_to_blocks

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

