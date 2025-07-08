import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_multiple_children(self):
        child_node = LeafNode("i", "child")
        parent_node = ParentNode("span", [child_node])
        cousin_node = LeafNode("b", "cousin")
        uncle_node = ParentNode("span", [cousin_node])
        grandparent_node = ParentNode("div", [parent_node, uncle_node])
        self.assertEqual(grandparent_node.to_html(), "<div><span><i>child</i></span><span><b>cousin</b></span></div>")

    def test_to_html_no_children(self):
        parent_node = ParentNode("span", None)
        my_exception = self.assertRaises(ValueError, parent_node.to_html)
        

if __name__ == "__main__":
    unittest.main()