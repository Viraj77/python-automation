# Basic Calculator Program in Python

# Step 1: Display menu to the user
print("Welcome to Basic Calculator")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Step 2: Take user's choice
choice = input("Enter your choice (1/2/3/4): ")

# Step 3: Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 4: Perform the operation based on user choice
if choice == '1':
    result = num1 + num2
    print("Result:", num1, "+", num2, "=", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", num1, "-", num2, "=", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", num1, "*", num2, "=", result)
elif choice == '4':
    # Step 5: Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print("Result:", num1, "/", num2, "=", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    # Step 6: Handle invalid choice
    print("Invalid choice. Please select 1, 2, 3, or 4.")
