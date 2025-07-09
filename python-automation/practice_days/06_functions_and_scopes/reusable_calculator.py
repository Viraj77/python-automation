# Reusable Calculator Program using Functions

# Step 1: Define functions for each operation

def add(a, b):
    """Function to add two numbers"""
    return a + b

def subtract(a, b):
    """Function to subtract second number from first"""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

def divide(a, b):
    """Function to divide first number by second (handles division by zero)"""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Step 2: Main program to interact with user
def calculator():
    print("Welcome to Reusable Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    # Step 3: Take input numbers from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Step 4: Call the appropriate function based on user choice
    if choice == '1':
        result = add(num1, num2)
        print("Result:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

# Step 5: Call the calculator function
calculator()
