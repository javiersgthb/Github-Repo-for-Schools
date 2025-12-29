"""
Module: Budget Editor Program
Author: Javier Silva
Date: [Current Date]

This program manages a budget list. It reads data from a text file, allows
the user to view, edit, and delete entries, and saves the final data to a
CSV file. It utilizes datetime formatting, exception handling, and file I/O.
"""

import csv
from datetime import datetime
import os

# Global constant for the input filename
INPUT_FILENAME = "final_exam.txt"

def get_current_time_string():
    """
    Returns the current date and time formatted as requested:
    month/date/year 12-hour/minutes/seconds am/pm
    Example: 01/08/23 04:24 PM
    """
    # %m: Month, %d: Day, %y: 2-digit Year
    # %I: 12-Hour, %M: Minute, %S: Second, %p: AM/PM
    return datetime.now().strftime("%m/%d/%y %I:%M:%S %p")

def create_sample_file():
    """
    Helper function to create the 'final_exam.txt' file.
    This creates an empty file if it is missing, as requested to remove sample data.
    """
    # Empty data or header only if required, prompt implied just the file existence.
    # We will create an empty file.
    data = ""
    try:
        with open(INPUT_FILENAME, "w") as file:
            file.write(data)
    except IOError as e:
        print(f"Error creating file: {e}")

def read_budget_data():
    """
    Reads data from the text file, strips characters, and splits by '|'.
    Returns a list of lists: [[Month, Amount], [Month, Amount], ...]
    """
    budget_data = []
    try:
        with open(INPUT_FILENAME, "r") as file:
            for line in file:
                # Strip newline characters and whitespace
                clean_line = line.strip()
                if clean_line:
                    # Split on the pipe character '|'
                    entry = clean_line.split('|')
                    # Basic validation to ensure we have 2 items
                    if len(entry) == 2:
                        budget_data.append(entry)
        return budget_data
    except FileNotFoundError:
        print(f"Error: {INPUT_FILENAME} not found. Creating a new one...")
        create_sample_file()
        return read_budget_data() # Recursive call to read the newly created file
    except Exception as e:
        print(f"An error occurred reading the file: {e}")
        return []

def list_budget_entries(data, show_indices=False):
    """
    Outputs the budget list formatted with headers.
    
    Args:
        data (list): The list of budget entries.
        show_indices (bool): If True, displays numbers for selection.
    """
    print("\n--- Current Budget Data ---")
    
    if not data:
        print("No budget entries found.")
        return

    # Define column widths for formatting
    w_num = 5
    w_month = 15
    w_amount = 15

    # Print Header using f-strings for alignment
    if show_indices:
        print(f"{'#':<{w_num}} {'Month':<{w_month}} {'Amount':<{w_amount}}")
    else:
        print(f"{'Month':<{w_month}} {'Amount':<{w_amount}}")
    
    print("-" * (w_month + w_amount + w_num))

    # Loop through list to print content
    for i, entry in enumerate(data):
        month = entry[0]
        amount = entry[1]
        
        if show_indices:
            # Display with 1-based index
            print(f"{i + 1:<{w_num}} {month:<{w_month}} {amount:<{w_amount}}")
        else:
            print(f"{month:<{w_month}} {amount:<{w_amount}}")
    print()

def edit_entry(data):
    """
    Allows the user to select an entry by index and edit its values.
    """
    print("\n--- Edit Entry ---")
    if not data:
        print("No entries to edit.")
        return

    # Show list with numbers
    list_budget_entries(data, show_indices=True)
    
    while True:
        try:
            user_input = input("Enter the number of the entry to edit (or -1 to exit): ")
            selection = int(user_input)
            
            if selection == -1:
                print("Exiting edit mode.")
                break
            
            # Convert 1-based selection to 0-based index
            index = selection - 1
            
            # Validate index exists in list
            if 0 <= index < len(data):
                current_month = data[index][0]
                current_amount = data[index][1]
                
                print(f"Editing: {current_month} | Current Amount: {current_amount}")
                
                new_month = input("Enter new Month: ").strip()
                new_amount = input("Enter new Amount: ").strip()
                
                # Update the list
                data[index] = [new_month, new_amount]
                print("Entry updated successfully.")
                break # Exit loop after successful edit
            else:
                print("Error: Invalid selection number. Please try again.")
                
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def delete_entry(data):
    """
    Allows the user to select an entry by index and delete it.
    """
    print("\n--- Delete Entry ---")
    if not data:
        print("No entries to delete.")
        return

    list_budget_entries(data, show_indices=True)
    
    while True:
        try:
            user_input = input("Enter the number of the entry to DELETE (or -1 to exit): ")
            selection = int(user_input)
            
            if selection == -1:
                print("Exiting delete mode.")
                break
            
            index = selection - 1
            
            if 0 <= index < len(data):
                removed_item = data[index]
                
                # Use the del function (keyword) to remove from list
                del data[index]
                
                print(f"Successfully removed entry for: {removed_item[0]}")
                break
            else:
                print("Error: Invalid selection number. Please try again.")
                
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def write_to_csv(data):
    """
    Writes the list data to a user-specified CSV file.
    """
    filename = input("Enter the desired filename for the CSV (e.g., budget.csv): ").strip()
    
    # Add extension if missing
    if not filename.endswith(".csv"):
        filename += ".csv"
        
    try:
        # newline='' prevents blank lines between rows
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            # Write header manually if desired, or just data. 
            # Prompt implies creating the file from the list.
            writer.writerow(["Month", "Amount"])
            writer.writerows(data)
            
        print(f"Successfully saved data to {filename}.")
        
    except IOError as e:
        print(f"Error writing to file: {e}")

def import_from_file(budget_data):
    """
    Imports budget data from a user-specified file path (TXT or CSV).
    - If a Month matches an existing entry, it OVERWRITES (updates) the Amount.
    - If the Month is new, it APPENDS it to the list.
    """
    print("\n--- Import Data ---")
    # Prompt explicitly for full path or filename
    file_path = input("Enter the full path or filename to import from (e.g., C:\\Data\\new_budget.csv): ").strip()
    
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
                    # Basic check if it's a header row (case insensitive)
                    if len(first_row) >= 2 and "month" in first_row[0].lower() and "amount" in first_row[1].lower():
                        pass # Skip header
                    elif len(first_row) >= 2:
                         # It wasn't a header, treat as data
                        entries_to_process.append([first_row[0], first_row[1]])
                
                for row in reader:
                    if len(row) >= 2: 
                        entries_to_process.append([row[0], row[1]])
                        
            else: 
                # Assume text file with '|' separated values (like original source)
                for line in file:
                    clean_line = line.strip()
                    if clean_line:
                        # Try split by pipe first
                        entry = clean_line.split('|')
                        if len(entry) >= 2:
                            entries_to_process.append(entry)

            # 2. Process entries: Overwrite or Append
            for new_entry in entries_to_process:
                new_month = new_entry[0]
                found_match = False
                
                # Check against existing list
                for i, existing_item in enumerate(budget_data):
                    # Case-insensitive match on Month
                    if existing_item[0].lower() == new_month.lower():
                        # Overwrite existing entry
                        budget_data[i] = new_entry
                        updated_entries_count += 1
                        found_match = True
                        break
                
                if not found_match:
                    budget_data.append(new_entry)
                    new_entries_count += 1
                            
            print(f"Import complete.")
            print(f"- New entries added: {new_entries_count}")
            print(f"- Existing entries updated: {updated_entries_count}")
            
    except Exception as e:
        print(f"An error occurred during import: {e}")

def main():
    """
    Main function to control the program flow.
    """
    # 1. Output Purpose
    print("Program Purpose: Budget Editor Program")
    
    # 2. Output Start Time
    start_time = get_current_time_string()
    print(f"Program Start Time: {start_time}")
    
    # 3. Read Data
    budget_data = read_budget_data()
    
    # 4. Main Loop
    while True:
        try:
            # List content at the start/end of loop
            list_budget_entries(budget_data)
            
            print("Options:")
            print("1. Edit Entry")
            print("2. Delete Entry")
            print("3. Import Data from File")
            print("4. Save to CSV and Exit")
            print("5. Force Exit (No Save)")
            
            choice = input("Enter selection: ")
            
            # Using if block to call desired functions
            if choice == '1':
                edit_entry(budget_data)
            elif choice == '2':
                delete_entry(budget_data)
            elif choice == '3':
                import_from_file(budget_data)
            elif choice == '4':
                write_to_csv(budget_data)
                print("Saving and closing program...")
                break # Break loop
            elif choice == '5':
                print("Force closing program...")
                break # Break loop
            else:
                print("Invalid option. Please enter 1, 2, 3, 4, or 5.")
                
        except Exception as e:
            # Output exception feedback
            print(f"An unexpected error occurred in the main menu: {e}")

    # Output End Time
    end_time = get_current_time_string()
    print(f"Program End Time: {end_time}")
    
    # Final Signature
    print("\nCompleted by, Javier Silva")

if __name__ == "__main__":
    main()