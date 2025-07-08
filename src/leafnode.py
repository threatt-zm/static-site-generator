from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("A tag value is required")
        if self.tag is None:
            return fr"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"