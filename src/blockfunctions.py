import re
from block import BlockType
from textnode import TextType, TextNode
from nodefunctions import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    strip_blocks = list(map(lambda x: x.strip(), split_blocks))
    new_blocks = list(filter(lambda x: x != "", strip_blocks))
    return new_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if all(list(map(lambda x: x.startswith(">"), lines))):
        return BlockType.QUOTE
    if all(list(map(lambda x: x.startswith("- "), lines))):
        return BlockType.UNORDERED_LIST
    if all(list(map(lambda x: x.startswith(f"{lines.index(x)+1}. "), lines))):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def text_to_children(text):
    html_nodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        if isinstance(node, TextNode):
            html_nodes.append(text_node_to_html_node(node))
        else:
            html_nodes.append(node)
    return html_nodes
def block_to_html_node(block, blocktype):
    match blocktype:
        case BlockType.CODE:
            code_text = block.strip("`").lstrip("\n")
            code_node = text_node_to_html_node(TextNode(code_text, TextType.CODE_TEXT))
            return ParentNode("pre", [code_node])
        case BlockType.HEADING:
            heading_number = block.count("#")
            heading_text = block.lstrip("# ")
            heading_node = text_to_children(heading_text)
            return ParentNode(f"h{heading_number}", heading_node)
        case BlockType.QUOTE:
            lines = block.lstrip("> ").split("\n")
            quote_children = []
            for text in lines:
                quote_nodes = text_to_children(text.lstrip(">"))
                quote_children.extend(quote_nodes)
            return ParentNode("blockquote", quote_children)
        case BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            ul_children = []
            for text in lines:
                ul_nodes = text_to_children(text.lstrip("- "))
                ul_children.append(ParentNode("li", ul_nodes))
            return ParentNode("ul", ul_children)
        case BlockType.ORDERED_LIST:
            lines = block.split("\n")
            ol_children = []
            number = 1
            for text in lines:
                ol_nodes = text_to_children(text.lstrip(f"{number}. "))
                ol_children.append(ParentNode("li", ol_nodes))
                number += 1
            return ParentNode("ol", ol_children)
        case BlockType.PARAGRAPH:
            text = " ".join(block.split("\n"))
            p_nodes = text_to_children(text)
            return ParentNode("p", p_nodes)
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    html_children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        html_children.append(block_to_html_node(block, blocktype))
    
    return ParentNode("div", html_children)