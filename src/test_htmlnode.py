import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a",None,None,{"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("p","this is a paragraph",None,None)
        expected_result = 'HTMLNode(tag: p, value: this is a paragraph, children: None, props: None)'
        self.assertEqual(repr(node), expected_result)

    def test_to_html(self):
        node = HTMLNode("h1", "Header 1", [HTMLNode()],)
        self.assertRaises(NotImplementedError, node.to_html)


if __name__ == "__main__":
    unittest.main()