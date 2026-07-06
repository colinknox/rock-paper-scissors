import random

emojis = {
    "r": "🪨",
    "p": "📃",
    "s": "✂️"
}
valid_choices = ("r", "p", "s")

while True:
    user_choice = input("Choose rock, paper, or scissors (r/p/s): ").lower()
    if user_choice not in valid_choices:
        print("Invalid choice! Choose either 'r', 'p', or 's'.")
        continue

    computer_choice = random.choice(valid_choices)

    print(f"User chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (
            user_choice == "r" and computer_choice == "s" or
            user_choice == "p" and computer_choice == "r" or
            user_choice == "s" and computer_choice == "p"
        ):
            print("You win!")
    else:
        print("You lose!")

    choices_to_continue = ("y", "n")
    will_user_continue = input("Continue? (y/n): ").lower()
    
    if will_user_continue not in choices_to_continue:
        print("Invalid choice! Choose either 'y' or 'n'.")
    elif will_user_continue == "n":
        break
    else:
        continue

     


# Ask user to make a choice
# If choice is not valid:
#     Print error
# Let computer make a choice
# Print choices using emojis
# Determine winner
# Ask user if they want to continue game
# If not
    # Terminate