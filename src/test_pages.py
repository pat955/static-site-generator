import unittest
from pages import extract_title

class TestPages(unittest.TestCase):
    def test1(self):
        markdown = "# Title"
        res = extract_title(markdown)
        ans = "Title"
        self.assertEqual(res, ans)