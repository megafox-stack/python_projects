from .save_loadexpenses import save_expenses

def add_expenses(expenses):
    
    amount = float(input("Amount:$ "))
    category = input("Category: ")
    desc = input("Description: ")
    date = input("Date (YYYY-MM-DD): ")

    expense = {
        "amount": amount,
        "category": category,
        "desc": desc,
        "date": date
    }

    expenses.append(expense)     
    save_expenses(expenses)
    print("Expense added!") 