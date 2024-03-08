import unittest

from main import split_nodes_image, split_nodes_links
from textnode import TextNode

class TestSplitNodes(unittest.TestCase):
    def test_images(self):
        node = TextNode("text test ![picture](https://example.png)", "text")
        res = split_nodes_image([node])
        answer = [TextNode("text test ", "text", None), TextNode("picture", "image", "https://example.png")]

        self.assertEqual(res, answer)

    def test_images2(self):
        node = TextNode("text test text test image here soon!! ![nope] here: ![img](https://example.png)", "text")
        res = split_nodes_image([node])
        answer = [TextNode("text test text test image here soon!! ![nope] here: ", "text"), TextNode("img", "image", "https://example.png")]

        self.assertEqual(res, answer)
    
    # def test_split_images2(self):
    #     text = TextNode("text test text test image here soon!! ![nope] here: ![image](https://example.png)  !!!! second image???? ![2](https://hello.png)", "text")
    #     res = split_nodes_image([text])
    #     answer = [
    #     TextNode("text test text test image here soon!! ![nope] here: ", "text"),
    #     TextNode("image", "image", "https://example.png"),
    #     TextNode("  !!!! second image???? ", "text"),
    #     TextNode("2", "image", "https://hello.png")
    #     ]
    #     self.assertEqual(res, answer)
    
    # def test_split_links(self):
    #     text = TextNode("text test text test image here soon!! ![nope] here: ![link!](https://example.png)  !!!! second image???? ![2](https://hello.png)", "text")
    #     res = split_nodes_links([text])
    #     answer = [
    #     TextNode("text test text test image here soon!! ![nope] here: ", "text"),
    #     TextNode("link!", "link", "https://example.png"),
    #     TextNode("  !!!! second image???? ", "text"),
    #     TextNode("2", "image", "https://hello.png")
    #     ]
    #     self.assertEqual(res, answer)