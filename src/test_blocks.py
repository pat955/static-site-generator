import unittest
from blocks import *
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
        node = TextNode("Hello John! ![a trick] [link](https://no.com)... [link](https::///)", "text")
        res = split_nodes_links([node])
        answer = [
        TextNode("Hello John! ![a trick] ", "text"),
        TextNode("link", "link", "https://no.com"),
        TextNode("... ", "text"),
        TextNode("link", "link", "https::///")
        ]
        self.assertEqual(res, answer)


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

class TestExtraction(unittest.TestCase):
    def test_images(self):
        text = "this is an image ![imageeee!](https://www.example.com)) and another image: ![image](https://i.imgur.com/zjjcJKZ.png)!!!!!"
        self.assertEqual(extract_markdown_images(text), [('imageeee!', 'https://www.example.com'), ('image', 'https://i.imgur.com/zjjcJKZ.png')])

    def test_links(self):
        text = "this is an image [link!!!](https://example.com)"
        self.assertEqual(extract_markdown_links(text), [('link!!!', 'https://example.com')])