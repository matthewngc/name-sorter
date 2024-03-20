import unittest
from name_sorter import Name, NameSorter

# Unit tests for instances of Name class
class TestName(unittest.TestCase):
    # Tests that attributes of Name is defined correctly
    def test_valid_name(self):
        name = Name("Matthew Ching Fung Ng")
        self.assertEqual(name.full_name, "Matthew Ching Fung Ng")
        self.assertEqual(name.last_name, "Ng")
        self.assertEqual(name.given_names, ["Matthew", "Ching", "Fung"])
    
    # Tests that the program throws an exception when the given names are greater than three
    def test_too_many_given_names(self):
        with self.assertRaises(SystemExit):
            Name("Matthew John James Johnson Ng")

    # Tests that the program throws an exception when there are no given names
    def test_no_given_names(self):
        with self.assertRaises(SystemExit):
            Name("Ng")

# Unit test for instances of the NameSorter class
class TestNameSorter(unittest.TestCase):
    # Tests that the get_name() method reads the names from the input file correctly
    def test_get_names(self):
        expected_input = ["James John Smith", "James Jamie Smith", "William Johnson"]
        name_sorter = NameSorter("test-names-list.txt", "test-output.txt")
        name_sorter.get_names()
        self.assertEqual(len(name_sorter.names), 3)
        for i in range(len(expected_input)):
            self.assertEqual(name_sorter.names[i].full_name, expected_input[i])
    
    # Tests that the sort_names() method correctly sorts the names alphabetically, first by last name, then by given name(s)
    def test_sort_names(self):
        expected_output = ["William Johnson", "James Jamie Smith", "James John Smith"]

        name_sorter = NameSorter("test-names-list.txt", "test-output.txt")
        name_sorter.get_names()
        name_sorter.sort_names()

        for i in range(len(expected_output)):
            self.assertEqual(name_sorter.names[i].full_name, expected_output[i])

    # Tests that the write_to_file() method correctly writes the sorted names to the output file.
    def test_write_names(self):
        expected_output = ["William Johnson", "James Jamie Smith", "James John Smith"]

        name_sorter = NameSorter("test-names-list.txt", "test_output.txt")
        name_sorter.get_names()
        name_sorter.sort_names()
        name_sorter.write_to_file()

        with open("test_output.txt", "r") as f:
            output = f.read().strip().split("\n")
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()