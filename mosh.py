import random

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
valid_choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors (r/p/s): ").lower()
        if user_choice in valid_choices:
            return user_choice     
        else:
            print("Invalid choice! Choose either 'r', 'p', or 's'.")

def display_choices(user_choice, computer_choice):
    print(f"User chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def get_game_result(user_choice, computer_choice):
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

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(valid_choices)

        display_choices(user_choice, computer_choice)

        get_game_result(user_choice, computer_choice)

        will_user_continue = input("Continue? (y/n): ").lower()
        if will_user_continue == "n":
            break

play_game()