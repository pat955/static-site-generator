import unittest

from blocks import block_to_block_type

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