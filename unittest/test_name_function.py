import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """test first_last"""
        formatted_name = get_formatted_name("addson", "filexd")
        self.assertEqual(formatted_name,"Addson Filexd")

#unittest.main

if __name__ =='__main__':
    unittest.main()