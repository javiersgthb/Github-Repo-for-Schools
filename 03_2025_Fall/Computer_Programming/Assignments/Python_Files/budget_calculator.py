"""
Module: Budget Calculator
Author: Javier Silva
Date: 11/12/2025

This program calculates a user's remaining monthly budget.
It uses exception handling to safely get a valid income and a list
of expenses, then displays a summary formatted with f-strings
and a detailed expense list formatted with the locale module.
"""

# Import locale for currency formatting
import locale

def get_valid_income():
    """
    Loops until the user enters a valid, non-negative income.
    Handles both non-numeric input (ValueError) and negative input
    (by raising a custom ValueError).

    Returns:
        float: The user's valid monthly income.
    """
    # Loop indefinitely until a valid float is returned
    while True:
        try:
            # Get input from the user
            income_str = input("Enter your total monthly income: ")
            
            # Try to convert the input to a float
            income = float(income_str)
            
            # Check for the logical error (negative income)
            if income < 0:
                # Raise a ValueError with a custom message
                raise ValueError("Income cannot be negative.")
                
            # If all checks pass, return the valid income and exit the loop
            return income
            
        # Catch the exception if the cast to float fails OR if we raised it
        except ValueError as e:
            # Print the specific error message
            print(f"Invalid input: {e}. Please try again.")

def get_expenses_list():
    """
    Loops to get all user expenses until they enter 'done' or '0'.
    Validates each expense to ensure it's a non-negative float.

    Returns:
        list: A list of all valid expense amounts (as floats).
    """
    # Create an empty list to store expenses
    expenses = []
    print("\n--- Enter Expenses ---")
    print("Enter each expense amount. Type 'done' or '0' to finish.")
    
    while True:
        expense_str = input("Enter expense amount: ")
        
        # Check for the exit condition
        if expense_str.lower() == 'done' or expense_str == '0':
            break
            
        # Use try...except to validate the input
        try:
            # Try to convert the input to a float)
            expense = float(expense_str)
            
            # Check for the logical error (negative expense)
            if expense < 0:
                # Raise a ValueError with a custom message
                raise ValueError("Expense cannot be negative.")
                
            # If valid, add to the list and give user feedback
            expenses.append(expense)
            print(f"  (Added: {expense:.2f})") # Format for clarity
            
        except ValueError as e:
            # Print the specific error message
            print(f"  Invalid input: {e}. Please try again.")
            
    return expenses

def main():
    """
    Main function to run the budget calculator.
    """
    print("Welcome to the Monthly Budget Calculator")
    
    # Set the locale for US currency formatting
    try:
        # Use 'en_US' for US locale
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 
    except locale.Error:
        # Fallback for systems that may not have 'en_US.UTF-8'
        locale.setlocale(locale.LC_ALL, '') 

    # --- Get Income and Expenses ---
    income = get_valid_income()
    expenses_list = get_expenses_list()

    # --- Calculations ---
    # Use the sum() function on the list
    total_expenses = sum(expenses_list)
    remaining_budget = income - total_expenses

    # --- Output Summary (using f-string formatting) ---
    print("\n--- Budget Summary ---")
    # Use :.2f for 2 decimal places and :_ for a comma separator
    # (Using _ as a comma separator is a cross-platform safe alternative
    # if the locale comma isn't rendering in all terminal types)
    # Using :.2f ensures rounding to 2 decimal places for currency.
    print(f"Total Income:     ${income:,.2f}")
    print(f"Total Expenses:   ${total_expenses:,.2f}")
    print(f"Remaining Budget: ${remaining_budget:,.2f}")

    # --- Output Individual Expenses (using locale) ---
    print("\n--- Individual Expenses List ---")
    if not expenses_list:
        print("No expenses were entered.")
    else:
        # Use enumerate to number the list
        for i, expense in enumerate(expenses_list, start=1):
            # Use locale.currency to format
            formatted_expense = locale.currency(expense, grouping=True)
            print(f"  {i}. {formatted_expense}")

# Standard check to run the main() function
if __name__ == "__main__":
    main()

# Final deliverable
print("\nCompleted by, Javier Silva")