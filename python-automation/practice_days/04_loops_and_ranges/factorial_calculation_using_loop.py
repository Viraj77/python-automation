# Factorial Calculator using Loop

# Step 1: Take input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Step 2: Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
# Step 3: Handle the case for 0! = 1
elif num == 0:
    print("The factorial of 0 is 1.")
# Step 4: Calculate factorial using a for loop
else:
    factorial = 1  # Initialize factorial variable
    for i in range(1, num + 1):  # Loop from 1 to num
        factorial *= i  # Multiply each number to factorial
    # Step 5: Display the result
    print(f"The factorial of {num} is {factorial}.")