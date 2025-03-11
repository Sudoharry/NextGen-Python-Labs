"""
Expense Tracking System
=======================
A console-based application to track and analyze personal/organizational expenses.

Features:
- Create expense records with amount, category, and description
- View chronological expense history
- Generate monthly financial reports
- Simple menu-driven interface

Author: Harendra Barot
Version: 1.1.1
Maintainer: IT Department
Last Updated: 2025-09-03
"""

import datetime

class Expense:
    """
    Represents a single financial expense entry with metadata
    
    Attributes:
        amount (float): Monetary value of the expense
        category (str): Classification group for expense
        description (str): Detailed explanation of expense
        date (datetime.date): Automatic creation timestamp
    """
    
    def __init__(self, amount, category, description):
        """
        Initialize a new Expense instance
        
        Args:
            amount (float): Positive monetary value
            category (str): Expense classification
            description (str): Contextual details
            
        Raises:
            ValueError: If amount is not positive numeric value
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.date.today()

    def __str__(self):
        """
        Standard string representation for expense records
        
        Returns:
            str: Formatted string in 'DATE - CATEGORY: $AMOUNT - DESCRIPTION' format
        """
        return f"{self.date} - {self.category}: ${self.amount:.2f} - {self.description}"


class ExpenseTracker:
    """
    Central controller class for managing expense records
    
    Provides core functionality for:
    - Expense creation and storage
    - Financial data retrieval
    - Period-based reporting
    
    Attributes:
        expenses (list): Collection of Expense objects
    """
    
    def __init__(self):
        """Initialize empty expense repository"""
        self.expenses = []

    def add_expense(self, amount, category, description):
        """
        Create and store new expense record
        
        Args:
            amount (float): Transaction value
            category (str): Expense classification
            description (str): Contextual details
            
        Returns:
            None: Prints confirmation message
        """
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        """
        Display all stored expenses in chronological order
        
        Returns:
            None: Prints list or empty state message
        """
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        for expense in self.expenses:
            print(expense)

    def monthly_report(self, month, year):
        """
        Generate consolidated financial report for calendar period
        
        Args:
            month (int): 1-12 representing calendar month
            year (int): 4-digit year
            
        Returns:
            None: Prints formatted report or period not found message
        """
        monthly_expenses = [e for e in self.expenses 
                          if e.date.month == month 
                          and e.date.year == year]
        
        if not monthly_expenses:
            print(f"No expenses found for {month}/{year}.")
            return
            
        total = sum(e.amount for e in monthly_expenses)
        print(f"Monthly Report for {month}/{year}:")
        for expense in monthly_expenses:
            print(expense)
        print(f"Total Expenses: ${total:.2f}")


# Driver Code
if __name__ == "__main__":
    """
    Main Application Entry Point
    
    Initializes expense tracker and presents interactive menu system
    Handles user input and delegates to tracker functionality
    """
    
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Monthly Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            # Expense creation workflow
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Rent, Entertainment): ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)

        elif choice == '2':
            # Display all records
            tracker.view_expenses()

        elif choice == '3':
            # Report generation workflow
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year (YYYY): "))
            tracker.monthly_report(month, year)

        elif choice == '4':
            # Clean exit
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            # Invalid input handling
            print("Invalid choice. Please try again.")