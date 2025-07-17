import unittest
from pagemethods import extract_title

class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Title        
"""
        title = extract_title(md)
        self.assertEqual(title, "Title")

        md = """
### Not a title        
"""
        self.assertRaises(ValueError, extract_title, md)


if __name__ == "__main__":
    unittest.main()