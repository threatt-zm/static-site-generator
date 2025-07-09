import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a text node", TextType.CODE_TEXT)
        self.assertEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "node_url.com")
        self.assertNotEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()