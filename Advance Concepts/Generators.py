# Generators: - A generator in Python is a special type of iterable that allows you to iterate over data lazily, its means returns the sequences of value
# We use yield function for the return the value of function.

# Key Concepts:
# Lazy Evaluation: Generators produce items only when requested, which can save memory.
# yield Keyword: Instead of returning a value and terminating, yield produces a value and suspends the function’s state for later resumption.
# State Retention: Generators remember where they left off after each yield, so you can keep calling them until they are exhausted.

# Example :-
def generator():
    yield 1
    yield 2
    yield 3
res = generator()

print(next(res))
print(next(res))
print(next(res))

# Explanation:
# my_generator(): This function is a generator because it uses yield. When you call it, it doesn’t immediately execute the code; instead, it returns a generator object.
# next(gen): This function is used to retrieve the next value from the generator.
# The first call to next() starts the generator and returns 1. The second call resumes the generator and returns 2, and so on.


# Example of Generator with a Loop:
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)

for number in gen:
    print(number)

# Explanation:
# countdown(n): This generator function counts down from n to 1, yielding each number.
# Looping: Since gen is a generator, it can be used in a loop. Each time the loop calls next(),
# the generator resumes where it left off, yields the next number, and pauses again.

# Key Differences Between Functions and Generators:
# Normal functions return a single value and terminate. Once return is executed, the function’s state is lost.
# Generators pause their execution and can resume later, which allows them to generate a series of values lazily.