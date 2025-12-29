# Import the randrange function to generate random numbers.
from random import randrange

def main():
    """
    Main function to encapsulate the full version of the number guessing game logic.
    """
    # Outer loop to control whether the user wants to play again.
    play_again = 'y'
    while play_again.lower() == 'y':
        
        # --- Game Setup ---
        # Announce the purpose of the program and the rules for the new game.
        print("--- New Game: Guess the Number! ---")
        print("I'm thinking of a number between 0 and 100.")
        print("You have 10 tries to guess it.")
        print("-------------------------------------")

        # Generate a random number from a range of 0 to 100.
        # randrange(0, 101) includes 0 and goes up to, but not including, 101.
        random_number = randrange(0, 101)
        
        # --- Main Game Loop ---
        # A 'for' loop limits the user to a specific number of guesses (10).
        # The range starts at 1 and goes to 11 to give us guess numbers 1 through 10.
        for guess_count in range(1, 11):
            
            # This inner while loop validates that the user enters a valid number.
            while True:
                try:
                    # Get user input and tell them which guess they are on.
                    guess_str = input(f"Guess #{guess_count}: Enter your guess: ")
                    guess = int(guess_str)
                    break # Exit the validation loop if the input is a valid integer.
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            # --- Guess Checking Logic ---
            # Check if the user's guess matches the random number.
            if guess == random_number:
                print(f"Success! You guessed the number {random_number} correctly.")
                print(f"It took you {guess_count} trie(s).")
                break  # Exit the for loop immediately since the game is won.

            # If the user is out of guesses, inform them they lost.
            elif guess_count == 10:
                print("\nYou've run out of tries. You lose.")
                print(f"The correct number was {random_number}.")

            # If the guess is incorrect, provide feedback on whether it was too high or too low.
            elif guess > random_number:
                print("Incorrect. Your guess was too high. Try again.")
            else: # The only remaining possibility is the guess was too low.
                print("Incorrect. Your guess was too low. Try again.")

        print("-------------------------------------")

        # --- Play Again Logic ---
        # Ask the user if they want to play again and validate the input.
        while True:
            play_again = input("Would you like to play again? (y/n): ")
            # Standardize input to lowercase to handle 'Y' or 'y'.
            if play_again.lower() == 'y' or play_again.lower() == 'n':
                break # Exit validation loop on valid input.
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
        print() # Add a space for readability before the next game.

    # Final statement showing who completed the program.
    print("Thank you for playing!")
    print("Completed by, Javier Silva")

# This standard line runs the main function when the script is executed.
if __name__ == "__main__":
    main()

