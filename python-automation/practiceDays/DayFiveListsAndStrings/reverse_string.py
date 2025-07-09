# Program to reverse a string

# Step 1: Take input from the user
original_string = input("Enter a string to reverse: ")

# Step 2: Reverse the string using slicing
# [::-1] means start from the end towards the first character, taking each character backward
reversed_string = original_string[::-1]

# Step 3: Display the reversed string
print("Reversed string is:", reversed_string)