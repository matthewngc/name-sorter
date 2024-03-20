import unittest
from name_sorter import Name, NameSorter

class TestName(unittest.TestCase):
    def test_valid_name(self):
        name = Name("Matthew Ching Fung Ng")
        self.assertEqual(name.full_name, "Matthew Ching Fung Ng")
        self.assertEqual(name.last_name, "Ng")
        self.assertEqual(name.given_names, ["Matthew", "Ching", "Fung"])
    
    def test_too_many_given_names(self):
        with self.assertRaises(SystemExit):
            Name("Matthew John James Johnson Ng")

    def test_no_given_names(self):
        with self.assertRaises(SystemExit):
            Name("Ng")
            
if __name__ == "__main__":
    unittest.main()