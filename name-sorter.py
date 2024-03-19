class Name:
    def __init__(self, full_name):
        self.full_name = full_name
        self.name_split = full_name.split()
        self.last_name = self.name_split[-1]
        self.given_names = self.name_split[:-1]

class NameSorter:
    def __init__(self, input):
        self.input = input
        self.names = []
    
    def get_names(self):
        try:
            with open(self.input, 'r') as file:
                self.names = [Name(line.strip()) for line in file.readlines()]
            for name in self.names:
                print(name.full_name)
        except:
            print("File could not be found, please check the file name and try again.")

    def sort_names(self):
        self.names.sort()

    

a = NameSorter("unsorted-names-list.txt")
a.get_names()