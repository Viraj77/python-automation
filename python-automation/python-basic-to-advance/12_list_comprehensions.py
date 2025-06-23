# List Comprehensions
# This script demonstrates how to use list comprehensions in Python.

# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Create a list of even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)
