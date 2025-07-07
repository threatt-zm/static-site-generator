from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_object):
        return self.text == other_object.text and self.text_type == other_object.text_type and self.url == other_object.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"