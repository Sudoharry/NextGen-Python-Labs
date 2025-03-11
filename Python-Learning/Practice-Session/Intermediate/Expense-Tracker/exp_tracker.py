import datetime 

class Expense:
    def __init__(self,amount,category,description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.date.today()


    def __str__(self):
        return f"{self.date} - {self.category} ${self.amount:.2f} - {self.description}"


class ExpenseTracker:

    def __init__(self):
        self.expense = []

    def add_expense(self,amount,category,description):
        expense = Expense(amount,category,description)
        self.expense.append(expense)
        print("Expense added successfully!")

    def view_expense(self):
        if not self.expense:
            print("No expense record found.")

        for expense in self.expense:
            print(expense)        


    def monthly_report(self,month,year):

        
        monthly_expenses = [e for e in self.expense 
                            if e.date.month == month
                            and e.date.year == year]

        if not monthly_expenses:
            print(f"No expense record found {month}/{year}")
            return
        

        total = sum(e.amount for e in monthly_expenses)
        print(f"Monthly Report for {month}/{year}:")
        for expense in monthly_expenses:
            print(expense)
        print(f"Total Expenses: ${total:.2f:}")    
        

if __name__ == '__main__':
    
    tracker = ExpenseTracker()

    while True:
        print("\nExpsense Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Monthly Report")
        print("4. Exit")

        choice = input("Choose an option:")

        if choice == '1':
            amount = float(input("Enter the expense amount:"))
            category = input("Enter the category:")
            description = input("Enter the expense description:")
            tracker.add_expense(amount,category,description)

        elif choice == '2':
            tracker.view_expense()


        elif choice == '3':
            month = input("Enter the month(1:12):")
            year = month = input("Enter the year(YYYY):")
            tracker.monthly_report(month,year)    

        elif choice == '4':
            # Clean exit
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            # Invalid input handling
            print("Invalid choice. Please try again.")





