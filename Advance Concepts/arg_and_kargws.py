# *args :- Its is the position arguments and its use pass a variable.
# Ex:-
def my_function(*args):
  for arg in args:
    print(arg)


my_function('Hello', 'World', 'Python')
# **kwargs :- Its is the keyword arguments and its use pass a variable.


def my_function(**kwargs):
  for key, value in kwargs.items():
    print(f'{key}: {value}')


my_function(name='Alice', age=30, city='New York')
