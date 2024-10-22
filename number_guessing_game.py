import random

def print_welcome_message():
    """Print the welcome message and game rules."""
    print("""
    Welcome to the Number Guessing Game!
    
    Rules:
    1. I have a number in mind between 1 and 1000.
    2. You need to guess this number.
    3. I'll give you hints if your guess is too high or too low.
    4. Keep guessing until you find the correct number.
    
    Good luck!
    """)

def generate_random_number():
    """Generate a random integer between 1 and 1000."""
    return random.randint(1, 1000)

def get_user_guess():
    """Get and validate user's guess."""
    while True:
        try:
            guess = int(input("Please enter your guess (1-1000): "))
            if 1 <= guess <= 1000:
                return guess
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game():
    """Main game logic."""
    target_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess > target_number:
            print("Too high! Try a lower number.")
        elif user_guess < target_number:
            print("Too low! Try a higher number.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break
def play_again():
    """ \nDo you want to play again ? """
    user_choice = input("\nType 'y' if you want to play again and 'n' if you plan to quit the game. ")
    if user_choice == "y":
        play_game()
    else:
        print("\nThank you for playing the game. I hope to see you again.\nDon't forget to drink some water. Bye !")

def main():
    print_welcome_message()
    play_game()
    play_again()

if __name__ == "__main__":
    main()