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


# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes
