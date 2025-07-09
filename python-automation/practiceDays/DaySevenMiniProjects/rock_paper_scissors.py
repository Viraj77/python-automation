import random

# Step 1: Define the choices
choices = ["rock", "paper", "scissors"]

# Step 2: Score tracking
user_score = 0
computer_score = 0

# Step 3: Define the function to determine the winner
def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Step 4: Main game loop
print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.\n")

while True:
    # Get user's move
    user_choice = input("Your move: ").lower()

    # Exit condition
    if user_choice == "exit":
        print("\n👋 Game Over!")
        print(f"Final Score ➤ You: {user_score} | Computer: {computer_score}")
        break

    # Check for valid move
    if user_choice not in choices:
        print("❌ Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
        continue

    # Computer's move
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Decide winner
    winner = get_winner(user_choice, computer_choice)

    if winner == "user":
        print("✅ You win this round!")
        user_score += 1
    elif winner == "computer":
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a draw!")

    # Show score
    print(f"Score ➤ You: {user_score} | Computer: {computer_score}\n")
