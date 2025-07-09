import unittest
from textnode import TextNode, TextType
from nodefunctions import text_node_to_html_node, split_nodes_delimiter

class TestNodeFunctions(unittest.TestCase):    
    def test_plain_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic_text(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code_text(self):
        node = TextNode("This is a text node", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "link_url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, {"href": "link_url"})

    def test_image(self):
        node = TextNode("This is a text node", TextType.IMAGE, "image_url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "image_url", "alt": "This is a text node"})

    def test_invalid_text(self):
        node = TextNode("This is a text node", None)
        self.assertRaises(Exception, text_node_to_html_node, node)

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAIN_TEXT),TextNode("bold", TextType.BOLD_TEXT),TextNode(" word", TextType.PLAIN_TEXT)])

    def test_italic_delimiter(self):
        node = TextNode("This is text with an _italic_ word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [TextNode("This is text with an ", TextType.PLAIN_TEXT),TextNode("italic", TextType.ITALIC_TEXT),TextNode(" word", TextType.PLAIN_TEXT)])

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.PLAIN_TEXT),TextNode("code block", TextType.CODE_TEXT),TextNode(" word", TextType.PLAIN_TEXT)])

    def test_multiple_delimiters(self):
        node = TextNode("This is text with a **bold** word and an _italic_ word", TextType.PLAIN_TEXT)
        first_split = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        second_split = split_nodes_delimiter(first_split, "_", TextType.ITALIC_TEXT)
        self.assertEqual(second_split, [TextNode("This is text with a ", TextType.PLAIN_TEXT),TextNode("bold", TextType.BOLD_TEXT),TextNode(" word and an ", TextType.PLAIN_TEXT),TextNode("italic", TextType.ITALIC_TEXT), TextNode(" word", TextType.PLAIN_TEXT)])

if __name__ == "__main__":
    unittest.main() 