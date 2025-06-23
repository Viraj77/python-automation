# File Handling
# This script demonstrates how to read from and write to files in Python.

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is a new line.\n")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
