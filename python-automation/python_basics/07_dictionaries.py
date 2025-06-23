# Dictionaries
# This script demonstrates how to use dictionaries in Python.

# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("Person:", person)

# Accessing values
print("Name:", person["name"])

# Adding a new key-value pair
person["email"] = "alice@example.com"
print("After adding email:", person)

# Looping through a dictionary
for key, value in person.items():
    print(key + ":", value)
