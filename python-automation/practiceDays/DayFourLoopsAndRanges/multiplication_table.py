# Program to print multiplication table of a number

# Step 1: Take input from the user
number = int(input("Enter a number to print its multiplication table: "))

# Step 2: Print a header
print(f"\nMultiplication Table of {number}:\n")

# Step 3: Use a for loop to print the table from 1 to 10
for i in range(1, 11):  # Loop from 1 to 10
    result = number * i  # Multiply the number with i
    print(f"{number} x {i} = {result}")  # Display the result in proper format