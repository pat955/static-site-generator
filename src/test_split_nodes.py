import unittest

from main import extract_markdown_images, extract_markdown_links
from textnode import TextNode

class TestSplitNodes(unittest.TestCase):
    def split_images(self):
        text = "text test text test image here soon!! ![nope] here: ![image](https://example.png)"
        res = extract_markdown_images(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("image", "image", "https://example.png"),]

        self.assertEqual(res, answer)
    
    def split_images2(self):
        print("testing...")
        text = "text test text test image here soon!! ![nope] here: ![image](https://example.png)  !!!! second image???? ![2](https://hello.png)"
        res = extract_markdown_images(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("image", "image", "https://example.png"),
        TextNode("  !!!! second image???? ", "text"),
        TextNode("2", "image", "https://hello.png")
        ]
        self.assertEqual(res, answer)
    
    def split_links(self):
        text = "text test text test image here soon!! ![nope] here: [link!](https://example.png)  !!!! second image???? ![2](https://hello.png)"
        res = extract_markdown_links(text)
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("link!", "link", "https://example.png"),
        TextNode("  !!!! second image???? ", "text"),
        TextNode("2", "image", "https://hello.png")
        ]
        self.assertEqual(res, answer)