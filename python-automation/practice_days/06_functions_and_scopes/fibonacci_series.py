# Function to check whether a number is in the Fibonacci series

def is_fibonacci(n):
    # Step 1: Handle base cases
    if n == 0 or n == 1:
        return True

    # Step 2: Initialize first two Fibonacci numbers
    a, b = 0, 1

    # Step 3: Generate Fibonacci numbers until it reaches or exceeds 'n'
    while b < n:
        a, b = b, a + b  # Move to next number in series

    # Step 4: Check if final number matches 'n'
    return b == n


# Main program starts here
# Step 5: Take input from the user
num = int(input("Enter a number to check if it is in the Fibonacci series: "))

# Step 6: Call the function and display result
if is_fibonacci(num):
    print(num, "is a Fibonacci number.")
else:
    print(num, "is NOT a Fibonacci number.")
