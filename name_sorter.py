import sys

# Define class for Names
class Name:
    # Initialize Name object with attributes
    def __init__(self, full_name):
        self.full_name = full_name
        self.name_split = full_name.split()
        self.last_name = self.name_split[-1]
        self.given_names = self.name_split[:-1]

        # Validation of name data
        if len(self.given_names) > 3 or len(self.given_names) == 0:
            print(f'Error with name "{self.full_name}"')
            if len(self.given_names) > 3:
                print("A name must only have up to 3 given names")
            else:
                print("A name must have at least one given name")
            sys.exit(1)

    # Method used to compare two instances of the Name class and determines if one is less than the other
    # Allows for the use of the sort() function for instances of the Name class
    def __lt__(self, other):
        return (self.last_name, self.given_names) < (other.last_name, other.given_names)

# Defines class for sorting names
class NameSorter:
    # Initialize NameSorter object with input file containing list of unsorted names
    def __init__(self, input):
        self.input = input
        self.names = []
    
    # Read names from input file
    def get_names(self):
        try:
            with open(self.input, 'r') as file:
                self.names = [Name(line.strip()) for line in file.readlines()]
        except Exception as e:
            print("File could not be found, please check the file name and try again.")
            sys.exit(1)

    # Sort names alphabetically
    def sort_names(self):
        self.names.sort()

    # Print the sorted names to the console
    def print_sorted_names(self):
        for name in self.names:
            print(name.full_name)

    # Write the sorted names to text file
    def write_to_file(self):
        try:
            with open("sorted-names-list.txt", "w") as file:
                for name in self.names:
                    file.write(name.full_name + '\n')
            print("Sorted names written to file sorted-names-list.txt")
        except:
            print("Unable to write sorted names to file")
            sys.exit(1)

# Define main function to execute sorting and output of sorted names
def main():
    if len(sys.argv) != 2:
        print("To run this program, use: python name_sorter.py <input-file-name>")
        sys.exit(1)

    input = sys.argv[1]

    name_sorter = NameSorter(input)
    name_sorter.get_names()
    name_sorter.sort_names()
    name_sorter.print_sorted_names()
    name_sorter.write_to_file()

if __name__ == "__main__":
    main()