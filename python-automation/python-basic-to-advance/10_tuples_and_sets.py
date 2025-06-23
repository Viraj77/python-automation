# Tuples and Sets
# This script demonstrates how to use tuples and sets in Python.

# Tuple (immutable sequence)
colors = ("red", "green", "blue")
print("Tuple:", colors)
print("First color:", colors[0])

# Set (unique, unordered collection)
numbers = {1, 2, 3, 2, 1}
print("Set:", numbers)  # Duplicates are removed
numbers.add(4)
print("After adding 4:", numbers)
