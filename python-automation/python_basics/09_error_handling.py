# Error Handling
# This script demonstrates how to handle errors using try-except in Python.

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("10 divided by", num, "is", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block always runs.")
