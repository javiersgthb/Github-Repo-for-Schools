"""
Module: Employee Logger
Author: Javier Silva
Date: 11/04/2025

This program logs new employees for an organization. It prompts for the number
of employees to add, then gathers a unique name and generates a unique ID
for each. It uses functions to modularize tasks and lists/dictionaries to
store and manage employee data, ensuring no duplicate names (case-insensitive)
or IDs are created.
"""

# Import the randrange function from the random module (covered in Ch 4)
from random import randrange

def create_employee(employees_list, existing_ids, existing_names):
    """
    Creates a new employee dictionary and adds it to the main employee list.

    This function prompts for a unique name (case-insensitive), generates a
    unique ID, and appends the new employee data to the mutable lists
    provided as arguments.

    Args:
        employees_list (list): The main list of employee dictionaries.
        existing_ids (list): A list of employee IDs already in use.
        existing_names (list): A list of employee names already in use.
    """
    
    # Get and validate the employee's name (Full Completion requirement)
    while True:
        name = input("Enter employee's name: ")
        
        # Use a list comprehension to create a lowercase version of the names list
        names_lower = [name.lower() for name in existing_names]
        
        # Check if the new name (in lowercase) is in the lowercase list
        if name.lower() in names_lower:
            print(f"Error: '{name}' already exists. Please enter a unique name.")
        else:
            existing_names.append(name) # Add the original-cased name to the list
            break

    # Generate and validate a unique employee ID
    while True:
        # Generates a random number from 1 up to 500 (1-500)
        new_id = randrange(1, 501) 
        
        # Check if the generated ID is already in our tracking list
        if new_id not in existing_ids:
            existing_ids.append(new_id) # Add the unique ID to the list
            break
        # If the ID is already in the list, the loop repeats to get a new one

    # Create the employee dictionary
    employee = {
        "name": name,
        "id": new_id
    }

    # Add the new employee dictionary to the main list (modifying the mutable list)
    employees_list.append(employee)
    print(f"Successfully created employee: {name} (ID: {new_id})")

def display_employee(employee):
    """
    Returns a formatted string for a single employee.

    Args:
        employee (dict): A dictionary object for a single employee.

    Returns:
        str: A formatted string reporting the employee's name and ID.
    """
    # Access the dictionary keys to get the name and ID
    name = employee.get("name", "N/A")
    emp_id = employee.get("id", "N/A")
    return f"Employee: {name}, ID: {emp_id}"

def main():
    """
    Main function to run the employee logging program.
    """
    # Start of program, print purpose
    print("Employee Logging Program")
    print("This program will create new employee records with unique names and IDs.")
    
    # --- Base Completion: Create empty lists ---
    employees_list = []     # This will be our list of employee dictionaries
    employee_ids = []       # Helper list to track existing IDs
    employee_names = []     # Helper list to track existing names (for validation)

    # Get the number of employees to add
    while True:
        num_to_add = input("How many new employees are you adding? ")
        if num_to_add.isdigit() and int(num_to_add) > 0:
            num_to_add = int(num_to_add)
            break
        else:
            print("Invalid input. Please enter a whole number greater than 0.")

    # --- Base Completion: Loop to call create_employee function ---
    for i in range(num_to_add):
        print(f"\n--- Adding Employee {i + 1} of {num_to_add} ---")
        # Pass the mutable lists to the function.
        # The function will modify them directly.
        create_employee(employees_list, employee_ids, employee_names)

    # --- Advanced Completion: Loop and call display_employee ---
    print("\n--- Final Employee Roster ---")
    if not employees_list:
        print("No employees were added to the log.")
    else:
        for emp in employees_list:
            # Call the display function for each employee and print the result
            print(display_employee(emp))

    # Print the full list of dictionaries as requested in Base Completion
    print("\n--- Full Employee Data (List of Dictionaries) ---")
    print(employees_list)

# Standard check to run the main() function when the script is executed
if __name__ == "__main__":
    main()

# --- Deliverables: Final print statement ---
print("\nCompleted by, Javier Silva")