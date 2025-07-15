import unittest
from blockfunctions import markdown_to_blocks, block_to_block_type, markdown_to_html_node
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

    def test_block_to_block_type(self):
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

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> This is a quote block
> that contains a **bolded phrase** and
> an italic _word_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote block that contains a <b>bolded phrase</b> and an italic <i>word</i></blockquote></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_heading(self):
        md = """
### This is a h3 heading with `code`

##### This is a h5 heading with _italic_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is a h3 heading with <code>code</code></h3><h5>This is a h5 heading with <i>italic</i></h5></div>"
        )

    def test_unordered_list(self):
        md = """
- Item with no inline markdown
- Item with **bolded**
- Item with _italic_        
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item with no inline markdown</li><li>Item with <b>bolded</b></li><li>Item with <i>italic</i></li></ul></div>"
        )

    def test_unordered_list(self):
        md = """
1. Item with no inline markdown
2. Item with **bolded** and ![image](https://i.imgur.com/zjjcJKZ.png)
3. Item with _italic_ and a link [to boot dev](https://www.boot.dev)       
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ol><li>Item with no inline markdown</li><li>Item with <b>bolded</b> and <img src="https://i.imgur.com/zjjcJKZ.png" alt="image"></img></li><li>Item with <i>italic</i> and a link <a href="https://www.boot.dev">to boot dev</a></li></ol></div>'
        )

if __name__ == "__main__":
    unittest.main() 