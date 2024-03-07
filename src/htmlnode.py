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
        if not self.tag:
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

        if not self.value:
            raise Exception(ValueError)

        if not tag:
            return self.value

        if tag == "a":

            return f"<{tag} {self.props_to_html()}>{self.value}</{tag}>"

        return f"<{tag}>{self.value}</{tag}>"
        
# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes
