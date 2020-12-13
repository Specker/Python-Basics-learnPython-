# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.

import re

find_function = []

for function in dir(re):
    if "find" in function:
        find_function.append(function)
        

print(sorted(find_function))

