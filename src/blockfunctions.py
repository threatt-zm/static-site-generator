import re
from block import BlockType

def markdown_to_blocks(markdown):
    split_blocks = markdown.split("\n\n")
    strip_blocks = list(map(lambda x: x.strip(), split_blocks))
    new_blocks = list(filter(lambda x: x != "", strip_blocks))
    return new_blocks

def block_to_block_type(markdown):
    lines = markdown.split("\n")

    if all(list(map(lambda x: re.match(r"^#{1,6} \w+", x), lines))):
        return BlockType.HEADING
    if all(list(map(lambda x: x.startswith("```") and x.endswith("```"), lines))):
        return BlockType.CODE
    if all(list(map(lambda x: x.startswith(">"), lines))):
        return BlockType.QUOTE
    if all(list(map(lambda x: x.startswith("- "), lines))):
        return BlockType.UNORDERED_LIST
    if all(list(map(lambda x: x.startswith(f"{lines.index(x)+1}. "), lines))):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH