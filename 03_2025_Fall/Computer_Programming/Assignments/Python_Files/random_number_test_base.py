# Import the randrange function to generate random numbers.
from random import randrange

def main():
    """
    Main function to encapsulate the base version of the number guessing game logic.
    """
    # --- Game Setup ---
    # Announce the purpose of the program.
    print("--- Guess the Number! ---")
    
    # Generate a random number from a range of 0 to 10.
    # randrange(0, 11) includes 0 and goes up to, but not including, 11.
    random_number = randrange(0, 11)
    
    # Initialize a counter to track the number of guesses.
    guess_count = 0

    # --- Main Game Loop ---
    # A 'while True' loop will repeat indefinitely until the user
    # guesses correctly and the 'break' statement is executed.
    while True:
        # This inner while loop validates that the user enters a valid number.
        while True:
            try:
                # Get user input and convert it to an integer.
                guess_str = input("Guess the number between 0 and 10: ")
                guess = int(guess_str)
                break # Exit the validation loop if the input is a valid integer.
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        # Increment the guess counter for each attempt.
        guess_count += 1

        # --- Guess Checking Logic ---
        # Check if the user's guess matches the random number.
        if guess == random_number:
            # If the guess is correct, print a success message and exit the loop.
            print(f"Success! You guessed the number correctly.")
            print(f"It took you {guess_count} trie(s).")
            break
        else:
            # If the guess is incorrect, provide feedback.
            print("Incorrect. Please try again.")

    # Final statement showing who completed the program.
    print("\nCompleted by, Javier Silva")

# This standard line runs the main function when the script is executed.
if __name__ == "__main__":
    main()

