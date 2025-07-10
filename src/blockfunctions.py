import re
from block import BlockType

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