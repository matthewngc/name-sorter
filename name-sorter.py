import sys

class Name:
    def __init__(self, full_name):
        self.full_name = full_name
        self.name_split = full_name.split()
        self.last_name = self.name_split[-1]
        self.given_names = self.name_split[:-1]
        if len(self.given_names) > 3:
            print("A name must only have up to 3 given names")
            sys.exit(1)

    def __lt__(self, other):
        return (self.last_name, self.given_names) < (other.last_name, other.given_names)

class NameSorter:
    def __init__(self, input):
        self.input = input
        self.names = []
    
    def get_names(self):
        try:
            with open(self.input, 'r') as file:
                self.names = [Name(line.strip()) for line in file.readlines()]
            # for name in self.names:
            #     print(name.full_name)
        except:
            print("File could not be found, please check the file name and try again.")

    def sort_names(self):
        self.names.sort()
        for name in self.names:
            print(name.full_name)

    

a = NameSorter("unsorted-names-list.txt")
a.get_names()
a.sort_names()