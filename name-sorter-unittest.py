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

class TestNameSorter(unittest.TestCase):
    def test_get_names(self):
        name_sorter = NameSorter("test-names-list.txt")
        name_sorter.get_names()
        self.assertEqual(len(name_sorter.names), 3)
        self.assertEqual(name_sorter.names[0].full_name, "James John Smith")
        self.assertEqual(name_sorter.names[1].full_name, "James Jamie Smith")
        self.assertEqual(name_sorter.names[2].full_name, "William Johnson")
    
    def test_sort_names(self):
        name_sorter = NameSorter("test-names-list.txt")
        name_sorter.get_names()
        name_sorter.sort_names()
        self.assertEqual(name_sorter.names[0].full_name, "William Johnson")
        self.assertEqual(name_sorter.names[1].full_name, "James Jamie Smith")
        self.assertEqual(name_sorter.names[2].full_name, "James John Smith")

if __name__ == "__main__":
    unittest.main()