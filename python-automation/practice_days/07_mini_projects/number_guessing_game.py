import random

def choose_difficulty():
    """Set the number of attempts based on chosen difficulty"""
    print("Choose difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Hard (5 attempts)")
    
    while True:
        choice = input("Enter 1 for Easy or 2 for Hard: ")
        if choice == '1':
            return 10
        elif choice == '2':
            return 5
        else:
            print("Invalid input. Please choose 1 or 2.")

def play_game():
    """Main function to play the number guessing game"""
    
    # Step 1: Generate a random number
    secret_number = random.randint(1, 100)
    
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Step 2: Set attempts based on difficulty
    attempts_left = choose_difficulty()
    
    # Step 3: Game loop
    while attempts_left > 0:
        try:
            guess = int(input(f"\nYou have {attempts_left} attempt(s) left. Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Guess must be between 1 and 100.")
            continue

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! The number was {secret_number}. You won in {10 - attempts_left + 1} attempt(s)!")
            break

        attempts_left -= 1

    else:
        # This runs if the loop finishes without a break
        print(f"\n😞 You're out of attempts! The number was {secret_number}.")

# Run the game
play_game()
