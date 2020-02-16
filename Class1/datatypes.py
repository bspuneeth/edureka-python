# Standard Data types

"""
Immutable data types
Values can't be changed
"""

# 1. Numbers
"""
Types of numbers
1. int
2. float
3. complex
* In python you can represent numbers in Binary, Octal and Hexadecimal
"""

A = 10
B = 20.75
C = 10 + 6j

print(A, B, C)

# 2. Strings

A = 'This is a string'
B = "This is also a string"

print(A)
print(B)

# 3. Tuples
"""
Tuples consists of a number of values separated by comma and is enclosed by parenthesis
"""

Atuple = (10, 9999, 3.15, 'edureka')

print(Atuple)

"""
Mutable data types
Values can be changed
"""

# 1. lists
"""
Lists are an order sets of elements enclosed within square brackets. 
Differences between Lists and Tuple:
1. Lists are enclosed in square brackets [] and tuples are enclosed in parenthesis ()
2. Lists are mutable and tuples are not mutable
3. Tuples are faster than Lists
"""

ListEx = [10, 9999, 3.15, 'edureka']

print(ListEx)
print(ListEx[2])

# 2. dictionaries
"""
Dictionaries are key value pairs. Each key and value is separated by colon(:) and each item is separated by comma(,)
Dictionaries are enclosed by curly braces {}
"""

DictionaryEx = {'Name': 'Puneeth', 'Age': 28}

print(DictionaryEx)

# 3. sets
"""
A Set is an unordered collection of items. Every element is unique.
Elements are separated by comma(,) inside curly braces{}   
"""

SetEx = {1, 3.15, 3, 4, 3}

print(SetEx)
