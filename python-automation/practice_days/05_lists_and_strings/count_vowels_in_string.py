# Program to count vowels in a string

# Step 1: Take input from the user
text = input("Enter a string: ")

# Step 2: Define the vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Step 3: Initialize a counter to keep track of vowels
vowel_count = 0

# Step 4: Loop through each character in the string
for char in text:
    # Step 5: Check if the character is a vowel
    if char in vowels:
        vowel_count += 1  # Increment the counter if it's a vowel

# Step 6: Display the total number of vowels
print("Number of vowels in the string:", vowel_count)
