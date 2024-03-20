# Name Sorter Coding Assessment

## Overview

The purpose of this Python script is to sort a list of names in a text file alphabetically, ordered by last name, followed by any given names.
Each name must have at least 1 given name, and up to 3 given names.

## Instructions

1. Clone this repository using the following command:

    ```git clone https://github.com/matthewngc/name-sorter```

2. Add the unsorted names to the file unsorted-names-list.txt

3. Run the Python script using the following command:

    ```python name_sorter.py unsorted-names-list.txt```

## Unit Testing

Unit testing has been performed for this program in name_sorter_unittest.py.
The following unit tests have been performed:

- Testing the validity of the names (at least one given name, no more than three given names).
- Testing that the names in the input file are read correctly.
- Testing that the names are sorted correctly (alphabetically, first by last name then by given names).
- Testing that the sorted names are written correctly to the output file.
