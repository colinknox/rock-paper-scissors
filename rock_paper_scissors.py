import random

possible_choices = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}

user_choice = str(input("Rock, paper, or scissors? (r/p/s): ")).lower()    
computer_choice = random.choice(list(possible_choices))

if user_choice not in possible_choices:
    print("Invalid choice!")
# elif (
#     user_choice == "r" and computer_
# ):
    
print(f"USER CHOICE = {user_choice}")
print(f"COMPUTER CHOICE = {computer_choice}")


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