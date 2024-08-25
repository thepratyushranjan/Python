# Dictionary comprehension in Python is a concise way to create dictionaries.
# It allows you to generate a new dictionary by applying an expression to each key-value pair in an existing iterable,
# optionally filtering them based on a condition. Similar to list comprehensions, dictionary comprehensions provide a Pythonic way to create dictionaries in a single line.
# Syntax :- {key_expression: value_expression for item in iterable}

# Ex-1
# Basic dictionary comprehension
squares = {x: x ** 2 for x in range(5)}

print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Ex-2
# Dictionary comprehension with a condition
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}

print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# EX-3
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Doubling values in the dictionary
doubled_values = {k: v * 2 for k, v in original_dict.items()}

print(doubled_values)  # Output: {'a': 2, 'b': 4, 'c': 6, 'd': 8}

# Ex-4
# Nested dictionary comprehension to create a multIterating Over a Dictionaryiplication table
multiplication_table = {x: {y: x * y for y in range(1, 6)} for x in range(1, 6)}

print(multiplication_table)
# Output:
# {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
#  2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
#  3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
#  4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
#  5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}}

# Ex-5 Comprehension for Swapping Keys and Values:
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Swapping keys and values
swapped_dict = {v: k for k, v in original_dict.items()}

print(swapped_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}

# Ex-6  Dictionary Comprehension with Multiple Conditions:
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Filtered dictionary with conditions on both keys and values
filtered_dict = {k: v for k, v in original_dict.items() if v % 2 == 0 and k > 'b'}

print(filtered_dict)  # Output: {'d': 4}
