
import sys
import os

# Add current directory to path for imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import all modules
from expenses_operations.add_expenses import add_expenses
from expenses_operations.view_expenses import view_expenses
from expenses_operations.save_loadexpenses import save_expenses, load_expenses
from expenses_operations.total_expenses import calculate_total
from expenses_operations.category_summary import category_summary
from expenses_operations.set_budget import set_budget, check_budget_warning
monthly_budget = None            
if __name__ == "__main__":
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Total Spent")
        print("4 Category Summary") 
        print("5 add budget")
        print("6 Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
           print("total spent:",calculate_total(expenses))
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            monthly_budget = set_budget()          
        else:
            save_expenses(expenses)
            print("Goodbye!")
            break
