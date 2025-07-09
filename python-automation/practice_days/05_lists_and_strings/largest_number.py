# Program to find the largest number in a list

# Step 1: Create a list of numbers
numbers = [10, 25, 47, 3, 89, 56, 32]

# Step 2: Assume the first number is the largest (initially)
largest = numbers[0]

# Step 3: Loop through each number in the list
for number in numbers:
    # Step 4: Compare current number with the assumed largest
    if number > largest:
        largest = number  # Update largest if current number is bigger

# Step 5: Print the largest number
print("The largest number in the list is:", largest)
