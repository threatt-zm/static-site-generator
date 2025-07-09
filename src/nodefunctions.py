import re
from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text type")

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_text = node.text.split(delimeter)
        for node_text in split_text:
            if node_text == "" or node_text is None:
                continue
            elif node_text.startswith(" ") or node_text.endswith(" "):
                new_nodes.append(TextNode(node_text, TextType.PLAIN_TEXT))
            elif node.text_type != text_type and node.text_type != TextType.PLAIN_TEXT:
                new_nodes.append(TextNode(node_text, node.text_type))
            else:
                new_nodes.append(TextNode(node_text, text_type))
    return new_nodes

def extract_markdown_images(image):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", image)
    return matches

def extract_markdown_links(link):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", link)
    return matches