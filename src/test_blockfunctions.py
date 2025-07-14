import unittest
from blockfunctions import markdown_to_blocks, block_to_block_type
from block import BlockType

class TestNodeFunctions(unittest.TestCase):    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading(self):
        md = "#### This is a heading"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.HEADING, blocktype)

        md = "```\nThis is a code block\n```"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.CODE, blocktype)

        md = "> This is a quote that\n> is broken into \n> multiple lines"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.QUOTE, blocktype)

        md = "- This is the first item of the unordered list\n- This is the second item of the unordered list\n- This is the third item of the unordered list"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.UNORDERED_LIST, blocktype)

        md = "1. This is the first item of the ordered list\n2. This is the second item of the ordered list\n3. This is the third item of the ordered list"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.ORDERED_LIST, blocktype)

        md = "This is a normal paragraph"
        blocktype = block_to_block_type(md)
        self.assertEqual(BlockType.PARAGRAPH, blocktype)

if __name__ == "__main__":
    unittest.main() 