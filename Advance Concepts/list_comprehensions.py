# List comprehension in Python is a concise way to create lists.
# It allows you to generate a new list by applying an expression to each item in an existing iterable, optionally filtering items using a condition.
# List comprehensions can replace the need for loops and provide a more Pythonic and readable approach to handling lists

# Syntax:- [expression for item in iterable]

# Q1: Squaring even numbers of list

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [i**2 for i in l1 if i % 2 == 0]
print(square)

# Q2:  Squaring even numbers of list
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square_list = [i**2 for sublist in list for i in sublist if i%2 == 0]
print(square_list)

# Q3: Generating a list first letter words in a list
words = ["apple", "banana", "cherry", "kiwi", 'mango']
fiirst_words = [i[0] for i in words]
print(fiirst_words)

# Q4: Converting a list in integer in list
string_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
conv_int = [int(i) for i in string_list]
print(conv_int)



