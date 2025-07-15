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
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimeter)
        for section in sections:
            if section == "":
                continue
            if sections.index(section) % 2 == 0:
                new_nodes.append(TextNode(section, TextType.PLAIN_TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))
    return new_nodes

def extract_markdown_images(image):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", image)
    return matches

def extract_markdown_links(link):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", link)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.PLAIN_TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.PLAIN_TEXT))
    return new_nodes

def text_to_textnodes(text):
    all_nodes = []
    text_node = TextNode(text, TextType.PLAIN_TEXT)
    bold_split = split_nodes_delimiter([text_node], "**", TextType.BOLD_TEXT)
    italic_split = split_nodes_delimiter(bold_split, "_", TextType.ITALIC_TEXT)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE_TEXT)
    image_split = split_nodes_image(code_split)
    link_split = split_nodes_link(image_split)
    all_nodes.extend(link_split)
    return all_nodes