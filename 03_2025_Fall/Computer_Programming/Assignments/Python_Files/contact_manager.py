"""
Module: Contact Manager
Author: Javier Silva
Date: 11/05/2025

This program provides a menu-driven interface to manage a CSV file
of contacts. It allows creating a new file, adding contacts,
viewing all contacts, and editing existing contacts.
All operations use standard Python file I/O and the csv module.
"""

# Import the csv module
import csv

# Define a global constant for the filename
FILENAME = 'contacts.csv'

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Contact Manager Menu ---")
    print("1. Create a new contact file")
    print("2. Add a new contact")
    print("3. View all contacts")
    print("4. Edit an existing contact")
    print("5. Exit program")

def create_contact_file():
    """
    Creates a new, empty contacts.csv file with a header row.
    This will overwrite any existing file.
    """
    try:
        # Open in 'w' (write) mode, which creates or overwrites the file
        # newline="" is critical for CSV files
        with open(FILENAME, 'w', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(['Name', 'Phone', 'Email'])
            
        print(f"'{FILENAME}' was created successfully.")
    
    # Handle file permission errors (e.g., file is read-only)
    except IOError as e:
        print(f"Error creating file: {e}")

def add_contact():
    """
    Appends a new contact (row) to the end of the CSV file.
    """
    # Get contact details from the user
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    
    # Create a list for the new row
    new_contact = [name, phone, email]
    
    try:
        # Open in 'a' (append) mode
        with open(FILENAME, 'a', newline='') as file:
            writer = csv.writer(file)
            
            # Use writerow (singular) to add the new contact
            writer.writerow(new_contact)
            
        print(f"Contact '{name}' was added successfully.")
        
    # Handle case where file doesn't exist to append to
    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. Please create the file first (Option 1).")
    except IOError as e:
        print(f"Error writing to file: {e}")

def view_contacts():
    """
    Reads and displays all contacts from the CSV file with basic formatting.
    """
    try:
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.reader(file)
            
            # Read and print the header
            header = next(reader)
            print(f"\n--- Contact List ---")
            # Use \t (tab) for basic formatting as requested
            print(f"{header[0]:<20}\t{header[1]:<15}\t{header[2]}")
            print("-" * 50) # Print a separator line
            
            # Loop through the remaining rows in the reader object
            for row in reader:
                print(f"{row[0]:<20}\t{row[1]:<15}\t{row[2]}")
                
    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. Please create the file first (Option 1).")
    except StopIteration:
        # This occurs if the file is empty (can't 'next(reader)')
        print("File is empty. No contacts to display.")
    except IOError as e:
        print(f"Error reading file: {e}")

def read_all_contacts():
    """
    Helper function to read all contacts from the CSV into a list of lists.
    This is used by the edit_contact function.
    
    Returns:
        A tuple containing (header, contacts_list)
        Returns (None, None) if file isn't found.
    """
    contacts_list = []
    header = []
    try:
        with open(FILENAME, 'r', newline='') as file:
            reader = csv.reader(file)
            # Read and store the header separately
            header = next(reader)
            # Read the rest of the contacts into the list
            for row in reader:
                contacts_list.append(row)
        return header, contacts_list
    
    except FileNotFoundError:
        print(f"Error: '{FILENAME}' not found. Please create the file first (Option 1).")
        return None, None
    except StopIteration:
        print("File is empty. No contacts to edit.")
        return None, None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None, None

def write_all_contacts(header, contacts_list):
    """
    Helper function to write an entire list of lists back to the CSV file.
    This is used by edit_contact to overwrite the file with new data.
    """
    try:
        with open(FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            # Write the header first
            writer.writerow(header)
            # Write the rest of the contact data
            writer.writerows(contacts_list)
        return True # Indicate success
    
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False # Indicate failure

def edit_contact():
    """
    Loads all contacts, displays them, asks which to edit,
    gets new info, and writes all contacts back to the file.
    """
    # 1. Read all content from the file into a list
    header, contacts_list = read_all_contacts()
    
    # If read_all_contacts failed (e.g., file not found), stop.
    if contacts_list is None:
        return
        
    # 2. Output existing contacts with a number (index + 1)
    print("\n--- Select a Contact to Edit ---")
    # Use enumerate to get an index (Ch 6)
    for i, contact in enumerate(contacts_list, start=1):
        print(f"{i}. {contact[0]} ({contact[1]}, {contact[2]})")

    # 3. Ask the user to select one
    try:
        choice_str = input(f"Enter the number of the contact to edit (1-{len(contacts_list)}): ")
        
        # Validate the choice
        if not choice_str.isdigit():
            print("Error: Invalid input. Please enter a number.")
            return

        choice = int(choice_str)
        
        # Check if the number is in the valid range
        if 1 <= choice <= len(contacts_list):
            # Convert 1-based choice to 0-based index
            index_to_edit = choice - 1
            
            # 4. Get new information
            print(f"Editing contact: {contacts_list[index_to_edit][0]}")
            new_phone = input(f"Enter new phone number ({contacts_list[index_to_edit][1]}): ")
            new_email = input(f"Enter new email ({contacts_list[index_to_edit][2]}): ")
            
            # 5. Update the list in memory
            contacts_list[index_to_edit][1] = new_phone
            contacts_list[index_to_edit][2] = new_email
            
            # 6. Write the *entire* modified list back to the file
            if write_all_contacts(header, contacts_list):
                print(f"Successfully updated contact '{contacts_list[index_to_edit][0]}'.")
            
        else:
            print("Error: Invalid contact number.")
            
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        
def main():
    """
    Main function to run the Contact Manager program.
    """
    print("Welcome to the Contact Manager Program")
    
    # Main application loop
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_contact_file()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print(f"Error: '{choice}' is an invalid option. Please try again.")

# Standard check to run the main() function
if __name__ == "__main__":
    main()

# Final deliverable
print("\nCompleted by, Javier Silva")
