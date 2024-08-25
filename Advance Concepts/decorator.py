# Decorators: - A decorator is essentially a function that takes another function as an argument, adds some functionality to it, and returns the modified function.
# Decorators are often used in scenarios like logging, authentication, or measuring performance and Caching/Memoization.

# How Decorators Work:
# Functions are First-Class Objects: Functions in Python can be passed around as arguments, assigned to variables, or returned from other functions.
# Higher-Order Functions: A function that takes another function as an argument or returns a function is known as a higher-order function.
# Closures: A decorator typically uses closures, where a nested function captures variables from its enclosing scope.
# Example:-

def my_decorator(func):
    def wrapper():
        print("Something before the function.")
        func()
        print("Something after the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Explanation:
# my_decorator(func): This is the decorator function. It takes a function (func) as an argument.
# wrapper(): Inside the decorator, we define another function (wrapper) that adds extra functionality around the original function.
# Returning wrapper: The my_decorator function returns the wrapper function, which now adds behavior before and after the original say_hello() function.
# @my_decorator: This is syntactic sugar for applying the decorator to the say_hello function. It is equivalent to writing say_hello = my_decorator(say_hello).

# Decorators with Arguments:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Something before the function.")
        res = func(*args, **kwargs)
        print("Something after the function.")
        return res
    return wrapper

@decorator
def add(a,b):
    return a+b
print(add(1,2))

# Explanation:
# 1: *args, **kwargs: The wrapper function uses these to accept any number of positional and keyword arguments, which are passed to the original function (add).
# 2: Return the result: The result of the decorated function (add) is captured and returned by wrapper.

