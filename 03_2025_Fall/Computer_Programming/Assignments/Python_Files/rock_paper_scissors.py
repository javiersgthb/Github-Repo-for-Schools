# Import the randrange function from the random library
from random import randrange

def get_user_weapon():
    """
    Displays the weapon choices to the user, gets their input, validates it,
    and returns the valid choice.
    No parameters.
    Returns the user's integer choice (1, 2, or 3).
    """
    while True: # Loop for input validation
        print("Choose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        # Using a try-except block is an advanced topic, but a simple check
        # for digits is within the scope of what you've learned.
        choice_str = input("Enter your choice (1, 2, or 3): ")

        if choice_str.isdigit():
            choice_int = int(choice_str)
            if 1 <= choice_int <= 3:
                return choice_int
            else:
                print("Invalid choice. Please enter a number between 1 and 3.\n")
        else:
            print("Invalid input. Please enter a number.\n")


def get_opponent_weapon():
    """
    Generates a random weapon choice for the opponent.
    No parameters.
    Returns a random integer between 1 and 3.
    """
    # randrange(1, 4) generates a random number from 1 up to (but not including) 4.
    # This results in a choice of 1, 2, or 3.
    return randrange(1, 4)

def determine_winner(user_weapon, opponent_weapon):
    """
    Compares the user's and opponent's weapons to determine the winner.
    Accepts user_weapon (int) and opponent_weapon (int) as parameters.
    Prints the outcome of the game.
    """
    # Helper values to make the logic clearer
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # Display choices to the user
    # This requires converting the numbers back to strings for a user-friendly message
    weapons = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}
    print(f"You chose: {weapons[user_weapon]}")
    print(f"Opponent chose: {weapons[opponent_weapon]}")

    # Determine the winner
    if user_weapon == opponent_weapon:
        print("The game is a tie!\n")
    # User win conditions
    elif (user_weapon == ROCK and opponent_weapon == SCISSORS) or \
         (user_weapon == SCISSORS and opponent_weapon == PAPER) or \
         (user_weapon == PAPER and opponent_weapon == ROCK):
        print("You win!\n")
    # If it's not a tie and the user didn't win, the opponent must have won.
    else:
        print("You lose!\n")


def main():
    """
    The main function that controls the flow of the game.
    """
    # Initialize the choice variable to 'y' to start the first game
    play_again = 'y'

    # Main game loop
    while play_again.lower() == 'y':
        # Get weapons for the user and the opponent
        user_weapon = get_user_weapon()
        opponent_weapon = get_opponent_weapon()

        # Determine the winner of the round
        determine_winner(user_weapon, opponent_weapon)

        # Ask the user if they want to play another round
        # Includes a validation loop
        while True:
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == 'y' or play_again.lower() == 'n':
                print() # Add a space for readability
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# This special if statement checks if the script is being run directly.
# If it is, it calls the main() function to start the program.
if __name__ == "__main__":
    main()

# Final print statement as required by the assignment
print("Completed by, Javier Silva")