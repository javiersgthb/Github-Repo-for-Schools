# grade_average_calculator.py

# This program calculates the average of a user-specified number of grades.
# It includes input validation and allows the user to perform calculations
# for multiple students in a single session.

def main():
    """ Main function to run the grade calculator program. """
    run_again = 'y'

    # Outer loop to allow calculations for more than one student.
    while run_again.lower() == 'y':
        
        # Announce the purpose of the program.
        print("--- Grade Average Calculator ---")
        
        # Initialize variables for the new student.
        total = 0.0
        
        # Get the number of grades the user wants to enter.
        while True:
            try:
                num_grades = int(input("How many grades will you be entering? "))
                if num_grades > 0:
                    break
                else:
                    print("Please enter a positive number of grades.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        print() # Add a space for readability.

        # Inner loop to get each grade from the user.
        for i in range(1, num_grades + 1):
            
            # Loop for grade validation (0-100).
            while True:
                try:
                    # Obtain input from the user for the next grade.
                    grade_str = input(f"Enter grade #{i}: ")
                    grade = float(grade_str)

                    # Check if the grade is within the valid range.
                    if 0 <= grade <= 100:
                        total += grade  # Add the valid grade to the total.
                        break # Exit validation loop on valid input.
                    else:
                        print("Invalid grade. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the grade.")
            
            # Calculate and display the current average after each entry.
            current_average = total / i
            print(f"  Current total: {total:.2f}, Grades entered: {i}, Current average: {current_average:.2f}\n")


        # Calculate the final average.
        # This check prevents a ZeroDivisionError, though the initial input validation for num_grades already handles this.
        if num_grades > 0:
            average = total / num_grades
        else:
            average = 0

        # Output the final results for the student.
        print("--- Final Results ---")
        print(f"Final grade total: {total:.2f}")
        print(f"Final number of grades: {num_grades}")
        print(f"Grade point average: {average:.2f}")
        print("---------------------\n")
        
        # Ask the user if they would like to continue for another student.
        # This loop validates that the input is 'y' or 'n'.
        while True:
            run_again = input("Calculate grades for another student? (y/n): ")
            if run_again.lower() == 'y' or run_again.lower() == 'n':
                print() # Add a space for the next run.
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

    # Final statement showing who completed the program.
    print("Program finished.")
    print("Completed by, Javier Silva")

# Run the main function when the script is executed.
if __name__ == "__main__":
    main()
