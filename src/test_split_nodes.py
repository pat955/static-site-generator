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
    
    def test_split_images2(self):
        node = TextNode("text test text test image here soon!! ![nope] here: ![image](https://example.png)  !!!! second image???? ![2](https://hello.png)", "text")
        res = split_nodes_image([node])
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ", "text"),
        TextNode("image", "image", "https://example.png"),
        TextNode("  !!!! second image???? ", "text"),
        TextNode("2", "image", "https://hello.png")
        ]
        self.assertEqual(res, answer)


    def test_split_links(self):
        node = TextNode("This is an image: ![dontcapture](https://dontcapture.com) this is a link: [capture](https://capture.com)", "text")
        res = split_nodes_links([node])
        answer = [
        TextNode("This is an image: ![dontcapture](https://dontcapture.com) this is a link: ", "text"),
        TextNode("capture", "link", "https://capture.com")
        ]
        self.assertEqual(res, answer)
    
    def test_split_links2(self):
        node = TextNode("text test text test image here soon!! ![nope] here: ![link!](https://example.png)  !!!! second image???? [2](https://hello.png)", "text")
        res = split_nodes_links([node])
        answer = [
        TextNode("text test text test image here soon!! ![nope] here: ![link!](https://example.png)  !!!! second image???? ", "text"),
    
        TextNode("2", "link", "https://hello.png")
        ]
        self.assertEqual(res, answer)
    
    def test_split_links3(self):
        node = TextNode("Hello John! ![a trick] [link](https://no.com)... [fakelink]](https::///)", "text")
        res = split_nodes_links([node])
        answer = [
        TextNode("Hello John! ![a trick] ", "text"),
        TextNode("link", "link", "https://no.com"),
        TextNode("... ", "text"),
        TextNode("fakelink]", "link", "https::///")
        ]
        self.assertEqual(res, answer)