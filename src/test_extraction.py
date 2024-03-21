import unittest
from split_nodes import extract_markdown_images, extract_markdown_links

class TestExtraction(unittest.TestCase):
    def test_images(self):
        text = "this is an image ![imageeee!](https://www.example.com)) and another image: ![image](https://i.imgur.com/zjjcJKZ.png)!!!!!"
        self.assertEqual(extract_markdown_images(text), [('imageeee!', 'https://www.example.com'), ('image', 'https://i.imgur.com/zjjcJKZ.png')])

    def test_links(self):
        text = "this is an image [link!!!](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [('link!!!', 'https://example.com')])