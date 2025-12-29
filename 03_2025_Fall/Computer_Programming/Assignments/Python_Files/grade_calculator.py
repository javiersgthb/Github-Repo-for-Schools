# Import the random module to use the choice() function later
import random

def main():
    """
    Main function to run the grade calculator program.
    """
    # Create an empty list to store grades
    grades = []

    # --- 1. Get Grade Input from User ---
    print("Enter grades one by one. Enter -1 to finish.")
    while True:
        grade_input = input("Enter a grade (-1 to stop): ")

        # Validate that the input is a number
        if grade_input.lstrip('-').isdigit():
            grade = int(grade_input)
            if grade == -1:
                break  # Exit the loop if the user enters -1
            else:
                # Add the valid grade to the list
                grades.append(grade)
        else:
            print("Invalid input. Please enter a number.")
    
    # Print the initial list of grades
    print("\nOriginal list of grades:")
    print(grades)

    # Proceed only if there are grades in the list
    if not grades:
        print("\nNo grades were entered. Exiting program.")
    else:
        # --- 2. Remove the Lowest Grade ---
        print("\n--- Removing the lowest grade ---")
        lowest_grade = min(grades)
        print(f"The lowest grade is: {lowest_grade}")
        # Find the index of the first occurrence of the lowest grade
        lowest_index = grades.index(lowest_grade)
        # Remove the item at that index
        grades.pop(lowest_index)
        print("List after removing the lowest grade:")
        print(grades)

    # Proceed only if there are still grades
    if not grades:
        print("\nNo grades left to process.")
    else:
        # --- 3. Remove a Random Grade ---
        print("\n--- Removing a random grade ---")
        random_grade = random.choice(grades)
        print(f"The random grade to remove is: {random_grade}")
        # Remove the first occurrence of the randomly chosen value
        grades.remove(random_grade)
        print("List after removing a random grade:")
        print(grades)

    # Proceed only if there are still grades
    if not grades:
        print("\nNo grades left to process.")
    else:
        # --- 4. Edit a Grade ---
        print("\n--- Editing a grade ---")
        while True:
            # List the current grades with a 1-based index for the user
            print("Current grades:")
            for i, grade in enumerate(grades, start=1):
                print(f"{i}. {grade}")
            
            edit_choice_str = input("Enter the number of the grade you want to edit: ")

            # Validate the user's choice
            if edit_choice_str.isdigit():
                edit_choice = int(edit_choice_str)
                if 1 <= edit_choice <= len(grades):
                    # Get the new grade from the user
                    while True:
                        new_grade_str = input(f"Enter the new value for grade #{edit_choice}: ")
                        if new_grade_str.isdigit():
                            new_grade = int(new_grade_str)
                            # Update the list (adjusting for 0-based index)
                            grades[edit_choice - 1] = new_grade
                            break # Exit the new grade input loop
                        else:
                            print("Invalid input. Please enter a number for the new grade.")
                    break # Exit the edit choice loop
                else:
                    print(f"Error: Please enter a number between 1 and {len(grades)}.\n")
            else:
                print("Error: Please enter a valid number.\n")

        print("List after editing a grade:")
        print(grades)

        # --- 5. Sort and Reverse the List ---
        print("\n--- Sorting and reversing the list ---")
        grades.sort()   # Sorts the list in numeric order
        grades.reverse() # Reverses the sorted list (highest to lowest)
        print("List after sorting and reversing:")
        print(grades)

        # --- 6. Get Grade Total and Average ---
        print("\n--- Final Grade Summary ---")
        # Use the sum() function to get the total
        total = sum(grades)
        print(f"Grade Total: {total}")

        # Use sum() and len() to calculate the average
        average = total / len(grades)
        print(f"Grade Average: {average:.2f}") # Formatted to 2 decimal places

# Call the main function to start the program
if __name__ == "__main__":
    main()

# Final print statement as required by the assignment
print("\nCompleted by, Javier Silva")