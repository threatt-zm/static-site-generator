from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is required")
        if self.children is None or self.children == []:
            raise ValueError("A child list is required")
        html_tags = f"<{self.tag}>"
        for child in self.children:
            html_tags += child.to_html()
        html_tags += f"</{self.tag}>"
        return html_tags