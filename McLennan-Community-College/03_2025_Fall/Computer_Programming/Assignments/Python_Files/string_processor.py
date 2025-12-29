"""
Module: String Processor
Author: Javier Silva
Date: 11/23/2025

This program allows a user to search for a substring within a main string.
If found, the user is given the option to replace that substring with a new one.
The program demonstrates string manipulation methods, input handling, and modular design.
"""

def get_user_input(prompt):
    """
    Prompts the user for input and returns the string.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        str: The input string provided by the user.
    """
    return input(prompt)

def find_substring(main_string, sub_string):
    """
    Checks if a substring exists within the main string and finds its index.

    Args:
        main_string (str): The string to search through.
        sub_string (str): The string to search for.

    Returns:
        int: The starting index of the substring if found, otherwise -1.
    """
    # Check if the substring is present using the 'in' keyword
    if sub_string in main_string:
        # Find the index using the .find() method
        index = main_string.find(sub_string)
        print(f"Success! The substring '{sub_string}' was found starting at index {index}.")
        return index
    else:
        print(f"The substring '{sub_string}' was NOT found.")
        return -1

def process_replacement(main_string, sub_string):
    """
    Asks the user if they want to replace the found substring and handles the logic.

    Args:
        main_string (str): The original string.
        sub_string (str): The substring to potentially replace.

    Returns:
        str: The updated string (if replaced) or the original string.
    """
    while True:
        # Get user choice, normalize to lowercase for easier comparison
        choice = get_user_input("Do you want to replace this substring? (yes/no): ").lower().strip()
        
        if choice == 'no':
            print("No replacement was made.")
            return main_string
        
        elif choice == 'yes':
            new_string = get_user_input(f"Enter the new string to replace '{sub_string}': ")
            
            # Replace the first occurrence of the substring (Chapter 10)
            # Note: Strings are immutable, so .replace() returns a new string.
            updated_string = main_string.replace(sub_string, new_string, 1)
            
            print(f"Updated String: {updated_string}")
            return updated_string
            
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """
    Main function to run the String Processor program.
    """
    print("Welcome to the String Processor Program.")
    print("This tool lets you search for and optionally replace text within a string.")
    print("-" * 60) # Formatting line (repetition operator)

    # 1. Get Inputs
    main_text = get_user_input("Enter the main string to search through: ")
    search_text = get_user_input("Enter the substring to search for: ")

    # 2. Find Substring
    index = find_substring(main_text, search_text)

    # 3. Process Replacement (only if found)
    if index != -1:
        # The logic for asking and replacing is handled in this function
        final_result = process_replacement(main_text, search_text)
    
    print("-" * 60)
    print("Thank you for using the String Processor Program.")

# Standard check to run the main() function
if __name__ == "__main__":
    main()

# Final deliverable
print("\nCompleted by, Javier Silva")