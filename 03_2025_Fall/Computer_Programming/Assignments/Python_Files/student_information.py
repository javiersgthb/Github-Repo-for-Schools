def main():
    """
    Main function to manage and display student information using a dictionary.
    """
    # Create an empty dictionary to store student information
    student_info = {}

    # --- 1. Create student entries ---
    # A dictionary of dictionaries is used. The outer dictionary key is the student's name.
    # The value is another dictionary containing that student's details.
    # This includes a list for the grades, as covered in Chapter 6.
    student_info["Javier Silva"] = {
        "id": "A00123456",
        "gpa": 4.0,
        "credits_completed": 60,
        "grades": [98, 95, 100, 97]
    }
    student_info["Anne Briggs"] = {
        "id": "A00987654",
        "gpa": 3.7,
        "credits_completed": 45,
        "grades": [92, 88, 95, 90]
    }
    student_info["Joel Murach"] = {
        "id": "A00555111",
        "gpa": 3.9,
        "credits_completed": 75,
        "grades": [99, 97, 96, 100]
    }

    # Print the full dictionary
    print("--- Initial Student Information Dictionary ---")
    print(student_info)

    # --- 2. List all student names ---
    print("\n--- Listing Student Names ---")
    # The default iteration for a dictionary loops through its keys.
    for name in student_info:
        print(name)

    # --- 3. Access and display all student information ---
    print("\n--- Accessing Full Student Information ---")
    # Use the \t escape sequence for uniform spacing in the header.
    print("Name\t\t\tID\t\tGPA\tCredits\tGrades")
    # The .items() method is used to access both the key (name) and value (details)
    for name, details in student_info.items():
        # Access the values from the inner dictionary using their keys.
        student_id = details['id']
        gpa = details['gpa']
        credits = details['credits_completed']
        grades = details['grades']
        print(f"{name}\t\t{student_id}\t{gpa}\t{credits}\t\t{grades}")

    # --- 4. Remove a student ---
    print("\n--- Removing a Student ---")
    # The pop() method removes the key-value pair for the specified key.
    removed_student = student_info.pop("Anne Briggs")
    print("Removed 'Anne Briggs' from the dictionary.")
    print("Updated dictionary:")
    print(student_info)

    # --- 5. Access specific GPA information ---
    print("\n--- Accessing Specific GPA Information ---")
    # Loop through the remaining students to get their GPA
    for name in student_info:
        # The .get() method safely retrieves a value.
        # First, get the inner dictionary for the student.
        details = student_info.get(name)
        # Then, get the GPA from that inner dictionary.
        gpa = details.get("gpa", "N/A") # Use "N/A" as a default if GPA key is missing
        print(f"GPA for {name}: {gpa}")

    # --- 6. Clear the student registry ---
    print("\n--- Clearing the Student Registry ---")
    # The clear() method removes all items from the dictionary.
    student_info.clear()
    print("Dictionary after clearing all students:")
    print(student_info)


# This special if statement checks if the script is being run directly.
# If it is, it calls the main() function to start the program.
if __name__ == "__main__":
    main()

# Final print statement as required by the assignment
print("\nCompleted by, Javier Silva")
