# Functions
# This script shows how to define and use functions in Python.

def greet(name):
    """Prints a greeting message."""
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)
