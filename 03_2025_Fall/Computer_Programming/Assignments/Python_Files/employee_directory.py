"""
Module: Employee Contact Directory
Author: Javier Silva
Date: 12/03/2025

This program manages an employee contact directory. It reads data from a text file,
allows the user to edit, delete, or import entries, and saves the final list to a CSV file.
It demonstrates file I/O, list manipulation, string formatting, and exception handling.
"""

import csv
from datetime import datetime
import os  # Import os to check if file exists before opening

# Constant for the source text file
SOURCE_FILE = "employee_contact_info.txt"

def get_formatted_time():
    """
    Returns the current time formatted as: MM/DD/YY 12-hour:Minute:Second AM/PM
    Example: 01/24/23 01:24 PM
    """
    return datetime.now().strftime("%m/%d/%y %I:%M:%S %p")

def create_source_file():
    """
    Creates the 'employee_contact_info.txt' file with the required initial data.
    This ensures the program runs correctly even if the file doesn't exist yet.
    """
    initial_data = """Jake jake@example.com
Steve steve@jobs.org
student student@mclennan.edu"""
    
    try:
        with open(SOURCE_FILE, "w") as file:
            file.write(initial_data)
    except IOError as e:
        print(f"Error creating source file: {e}")

def read_employees():
    """
    Reads from the default text file, strips whitespace, and splits lines into
    [name, email] lists.
    
    Returns:
        list: A list of lists, where each inner list is [name, email].
    """
    employees = []
    try:
        with open(SOURCE_FILE, "r") as file:
            for line in file:
                # Strip newline characters and whitespace
                clean_line = line.strip()
                if clean_line:  # Ensure line is not empty
                    # Split string into a list [Name, Email] using default whitespace delimiter
                    entry = clean_line.split()
                    employees.append(entry)
        return employees
    except FileNotFoundError:
        print(f"Error: {SOURCE_FILE} not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading: {e}")
        return []

def list_employees(employees_list, show_index=False):
    """
    Lists the content of the employee list formatted with f-strings.
    
    Args:
        employees_list (list): The list of employee data.
        show_index (bool): If True, prints a number index next to the name (for selection).
    """
    print("\n--- Current Directory ---")
    # Header with formatting (Left align 5 for ID, 15 for Name, 25 for Email)
    if show_index:
        print(f"{'#':<5} {'Name':<15} {'Email':<25}")
        print("-" * 45)
    else:
        print(f"{'Name':<15} {'Email':<25}")
        print("-" * 40)

    for i, emp in enumerate(employees_list):
        # Handle cases where a list might not have exactly 2 elements (robustness)
        name = emp[0] if len(emp) > 0 else "N/A"
        email = emp[1] if len(emp) > 1 else "N/A"
        
        if show_index:
            # Output with index (i + 1 for user friendliness)
            print(f"{i + 1:<5} {name:<15} {email:<25}")
        else:
            print(f"{name:<15} {email:<25}")
    print()

def edit_entry(employees_list):
    """
    Allows the user to select an entry by index and edit its values.
    """
    print("\n--- Edit Entry ---")
    list_employees(employees_list, show_index=True)
    
    while True:
        try:
            selection = int(input("Enter the number of the entry to edit (or -1 to exit): "))
            
            if selection == -1:
                print("Exiting edit mode without changes.")
                break
            
            # Adjust for 0-based index
            index = selection - 1
            
            # Validate index
            if 0 <= index < len(employees_list):
                current_entry = employees_list[index]
                print(f"Editing: {current_entry[0]} ({current_entry[1]})")
                
                # Get new values
                new_name = input("Enter new name: ").strip()
                new_email = input("Enter new email: ").strip()
                
                # Update the list
                employees_list[index] = [new_name, new_email]
                print("Entry updated successfully.")
                break
            else:
                print("Invalid selection. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred during editing: {e}")

def delete_entry(employees_list):
    """
    Allows the user to select an entry by index and delete it.
    """
    print("\n--- Delete Entry ---")
    list_employees(employees_list, show_index=True)
    
    while True:
        try:
            selection = int(input("Enter the number of the entry to delete (or -1 to exit): "))
            
            if selection == -1:
                print("Exiting delete mode without changes.")
                break
            
            # Adjust for 0-based index
            index = selection - 1
            
            # Validate index
            if 0 <= index < len(employees_list):
                removed_entry = employees_list[index]
                
                # Delete from list
                del employees_list[index]
                
                print(f"Successfully removed: {removed_entry[0]}")
                break
            else:
                print("Invalid selection. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred during deletion: {e}")

def write_to_csv(employees_list):
    """
    Writes the current employee list to a CSV file specified by the user.
    """
    filename = input("Enter the desired filename for the CSV (e.g., output.csv): ").strip()
    
    # Ensure extension exists
    if not filename.endswith('.csv'):
        filename += '.csv'
        
    try:
        # newline='' prevents blank lines between rows in Windows
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Name", "Email"])
            # Write data rows
            writer.writerows(employees_list)
        print(f"Successfully saved data to {filename}.")
        
    except IOError as e:
        print(f"Error writing to CSV: {e}")

def import_from_file(employees_list):
    """
    Imports employee data from a user-specified file path (TXT or CSV).
    - If a name matches an existing entry, it OVERWRITES (updates) it.
    - If the name is new, it APPENDS it to the list.
    """
    print("\n--- Import Data ---")
    # Prompt explicitly for full path or filename
    file_path = input("Enter the full path or filename to import from (e.g., C:\\Data\\new.csv): ").strip()
    
    # Remove quotes if user copied as path (common in Windows)
    file_path = file_path.replace('"', '')

    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist. Please check the path.")
        return

    try:
        with open(file_path, "r", newline="") as file:
            new_entries_count = 0
            updated_entries_count = 0
            entries_to_process = []
            
            # 1. Parse the file into a standardized list of entries
            if file_path.lower().endswith('.csv'):
                reader = csv.reader(file)
                # Skip header if present
                first_row = next(reader, None)
                if first_row:
                    if "name" in first_row[0].lower() and "email" in first_row[1].lower():
                        pass 
                    else:
                        if len(first_row) >= 2: entries_to_process.append([first_row[0], first_row[1]])
                
                for row in reader:
                    if len(row) >= 2: 
                        entries_to_process.append([row[0], row[1]])
                        
            else: 
                # Assume text file with space-separated values
                for line in file:
                    clean_line = line.strip()
                    if clean_line:
                        entry = clean_line.split()
                        if len(entry) >= 2:
                            entries_to_process.append(entry)

            # 2. Process entries: Overwrite or Append
            for new_entry in entries_to_process:
                new_name = new_entry[0]
                found_match = False
                
                # Check against existing list
                for i, existing_emp in enumerate(employees_list):
                    # Case-insensitive match on Name
                    if existing_emp[0].lower() == new_name.lower():
                        # Overwrite existing entry
                        employees_list[i] = new_entry
                        updated_entries_count += 1
                        found_match = True
                        break
                
                if not found_match:
                    employees_list.append(new_entry)
                    new_entries_count += 1
                            
            print(f"Import complete.")
            print(f"- New entries added: {new_entries_count}")
            print(f"- Existing entries updated: {updated_entries_count}")
            
    except Exception as e:
        print(f"An error occurred during import: {e}")

def main():
    """
    Main program logic.
    """
    # 1. Output purpose and Start Time
    print("Program Purpose: Employee Contact Directory Manager")
    print(f"Program Start Time: {get_formatted_time()}")
    
    # 2. Create and Read Data
    create_source_file()
    employees_list = read_employees()
    
    # 3. Main Loop
    while True:
        try:
            # Call list function at end/start of loop as requested
            list_employees(employees_list)
            
            print("Options:")
            print("1. Edit Entry")
            print("2. Delete Entry")
            print("3. Save to CSV and Exit")
            print("4. Force Exit (No Save)")
            print("5. Import Data from File")
            
            choice = input("Enter selection: ")
            
            if choice == '1':
                edit_entry(employees_list)
            elif choice == '2':
                delete_entry(employees_list)
            elif choice == '3':
                write_to_csv(employees_list)
                print("Closing program...")
                break # Break out of loop and close
            elif choice == '4':
                print("Force closing program...")
                break # Break out of loop and close
            elif choice == '5':
                import_from_file(employees_list)
            else:
                print("Invalid option. Please try again.")
                
        except Exception as e:
            print(f"An unexpected error occurred in the main menu: {e}")

    # 4. End Time and Signature
    print(f"Program End Time: {get_formatted_time()}")
    print("\nWritten by Javier Silva")

if __name__ == "__main__":
    main()