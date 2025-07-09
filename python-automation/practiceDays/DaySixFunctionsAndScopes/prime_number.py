# Function to check whether a number is prime or not

def is_prime(number):
    # Step 1: Handle numbers less than 2
    if number < 2:
        return False

    # Step 2: Check divisibility from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # If divisible, it's not a prime

    return True  # If no divisor found, it's a prime number


# Main program starts here
# Step 3: Take input from user
num = int(input("Enter a number to check if it's prime: "))

# Step 4: Call the function and display result
if is_prime(num):
    print(num, "is a Prime number.")
else:
    print(num, "is NOT a Prime number.")
