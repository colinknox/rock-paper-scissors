import random

def continue_game(answer):
    user_choice = answer.lower()
    choices = ["y", "n"]

    if user_choice not in choices:
        print("Invalid choice! Please type either 'y' or 'n'")

possible_choices = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}

while True:
    user_choice = str(input("Rock, paper, or scissors? (r/p/s): ")).lower()    
    computer_choice = random.choice(list(possible_choices))

    if user_choice not in possible_choices:
        print("Invalid choice!")
    elif (
        user_choice == "r" and computer_choice == "s" or
        user_choice == "p" and computer_choice == "r" or
        user_choice == "s" and computer_choice == "p"
    ):
        print("You win!")
    elif (
        user_choice == "r" and computer_choice == "p" or
        user_choice == "p" and computer_choice == "s" or
        user_choice == "s" and computer_choice == "r"
    ):
        print("You lose!")
    else:
        pass

    print(f"USER CHOICE = {user_choice}")
    print(f"COMPUTER CHOICE = {computer_choice}")


    does_user_continue = input("Continue? (y/n): ").lower()
    continue_game(does_user_continue)

    print(f"DOES USER CONTINUE?: {does_user_continue}")

# Tuple of valid answers and their respective emojis.
# Ask user "Rock, paper, or scissors (r/p/s): "
# Loop
    # If invalid input
        # Print "Invalid choice!"
    # If 
        # user_choice == "r" and computer_choice == "s" or
        # user_choice == "p" and computer_choice == "r" or
        # user_choice == "s" and computer_choice == "p"
        # Print user_choice
        # Print computer_choice
        # Print "You win!"
    # If 
        # user_choice == "r" and computer_choice == "p" or
        # user_choice == "p" and computer_choice == "s" or
        # user_choice == "s" and computer_choice == "r"
        # Print user_choice
        # Print computer_choice
        # Print "You lose!"
    # Else
        # pass

    # Prompt user with "Continue (y/n): "
    # If user choices "y":
        # Go back into the loop.
    # Else:
        # break