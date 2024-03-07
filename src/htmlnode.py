class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props
    
    def __repr__(self):
        return f"HTMLNode: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        html = ''
        for key, val in self.props.items():
            html += f'{key}="{val}" '
        return html[0:-1]


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise Exception(ValueError)
        elif not self.children:
            raise Exception(ValueError, "No children")
        
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        self.children = None
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        tag = self.tag

        if self.value == None:
            raise Exception(ValueError)

        if tag == None:
            return self.value

        if self.props != None:

            return f"<{tag} {self.props_to_html()}>{self.value}</{tag}>"

        return f"<{tag}>{self.value}</{tag}>"

def text_node_to_html_node(node):
    types = ["text", "bold", "italic", "code", "link","image"]
    if node.text_type not in types:
        raise Exception("Not A Supported Type")

    if node.text_type == "text":
        return LeafNode(value=text_node.text)

    elif node.text_type == "bold":
        return LeafNode("b", node.text)

    elif node.text_type == "italic":
        return LeafNode("i", node.text)
    
    elif node.text_type == "code":
        return LeafNode("code", node.text)

    elif node.text_type == "link":
        return LeafNode("a", node.text, {"href": node.url})
    
    elif node.text_type == "image":
        return LeafNode("img", "", {"src": node.url, "alt": node.text})
