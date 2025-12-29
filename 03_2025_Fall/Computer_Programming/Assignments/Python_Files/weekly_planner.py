"""
Module: Weekly Planner App
Author: Javier Silva
Date: 11/29/2025

This program acts as a weekly planner. It allows users to add tasks with
due dates, view tasks specifically due in the current week (Mon-Sun),
and list all scheduled tasks in chronological order.
"""

# Import datetime and timedelta for date manipulation
from datetime import datetime, date, timedelta

def add_task(tasks_list):
    """
    Prompts user for task details and adds them to the list.
    Validates the date format using try-except.
    """
    print("\n--- Add New Task ---")
    task_name = input("Enter the task name: ")
    
    while True:
        date_str = input("Enter due date (YYYY-MM-DD): ")
        try:
            # Parse string to datetime object
            # .date() converts it to a date object (removes time)
            due_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            
            # Create a dictionary for the task
            new_task = {
                "name": task_name,
                "due_date": due_date
            }
            
            # Add to the main list
            tasks_list.append(new_task)
            print(f"Task '{task_name}' added successfully for {due_date}.")
            break # Exit loop on success
            
        except ValueError:
            # Handle invalid date formats
            print("Error: Invalid date format. Please use YYYY-MM-DD.")

def view_weekly_tasks(tasks_list):
    """
    Calculates the current week's range (Mon-Sun) and displays tasks
    falling within that range.
    """
    print("\n--- Tasks Due This Week ---")
    
    # Get today's date
    today = date.today()
    
    # Calculate start of week (Monday)
    # .weekday() returns 0 for Monday, 6 for Sunday
    # Subtracting the weekday number from today gives us the most recent Monday
    start_of_week = today - timedelta(days=today.weekday())
    
    # Calculate end of week (Sunday)
    # Sunday is 6 days after Monday
    end_of_week = start_of_week + timedelta(days=6)
    
    print(f"(Current Week: {start_of_week} to {end_of_week})")
    
    found_task = False
    for task in tasks_list:
        # Compare dates using comparison operators
        if start_of_week <= task["due_date"] <= end_of_week:
            # Format date for display
            formatted_date = task["due_date"].strftime("%B %d, %Y")
            print(f"- {task['name']} (Due: {formatted_date})")
            found_task = True
            
    if not found_task:
        print("No tasks are due this week.")

def list_all_tasks(tasks_list):
    """
    Lists all tasks sorted chronologically.
    """
    print("\n--- All Scheduled Tasks ---")
    
    if not tasks_list:
        print("No tasks have been scheduled yet.")
    else:
        # Bonus Objective: Sort tasks by due_date using lambda
        # sorted() returns a new list, leaving the original touched or we can overwrite
        # key=lambda x: x["due_date"] tells Python to sort based on the date value
        sorted_tasks = sorted(tasks_list, key=lambda x: x["due_date"])
        
        for task in sorted_tasks:
            # Format date for display
            formatted_date = task["due_date"].strftime("%Y-%m-%d (%A)")
            print(f"- {formatted_date}: {task['name']}")

def main():
    """
    Main function to run the Weekly Planner App.
    """
    print("Welcome to the Weekly Planner App!")
    print("Manage your schedule by adding tasks and tracking due dates.")
    
    # Initialize empty list to store task dictionaries
    tasks = []
    
    while True:
        print("\n--- Menu ---")
        print("1. Add a Task")
        print("2. View Tasks Due This Week")
        print("3. List All Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_weekly_tasks(tasks)
        elif choice == '3':
            list_all_tasks(tasks)
        elif choice == '4':
            print("Goodbye! Stay organized.")
            break
        else:
            print("Invalid choice. Please enter a number 1-4.")

# Standard check to run the main() function
if __name__ == "__main__":
    main()

# Final deliverable
print("\nCompleted by, Javier Silva")