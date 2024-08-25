# Lambda Function: - A lambda function is a small anonymous function.
# Its take any number of arguments but can only have one expression
# Lambda functions are typically used for short-term tasks, often passed as arguments to higher-order functions (like map(), filter(), reduce()),
# and avoid the need to define regular functions using the def keyword.

# Syntax:- lambda arguments : expression

# Q_1:- length of string
string = "Pratyush Ranjan"
len_string = lambda  string : len(string)
print(len_string(string))

# Q2:- find the square even no in list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = (map(lambda lst:lst**2, filter(lambda lst : lst%2 == 0, lst)))
print(list(res))

# Q3:- Sort a list of string based on their alphabetic character and length

fruits = ["apple", "banana", "cherry", "kiwi", 'mango']
fruits_res = sorted(fruits, key= lambda fruits:len(fruits))
print(fruits_res)

# Q4:- maximum number value in a list of dictionaries on a specific key
data = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
values = max(data, key = lambda x: data[x])
print(values)