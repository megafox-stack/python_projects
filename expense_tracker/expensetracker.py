import json
monthly_budget = None
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
    check_budget_warning(expenses,monthly_budget)     
    print("Expense added!")  

def view_expenses(expenses):
    if not expenses:
        print("no expenses recorded")
        return
    print("\n-----All Expenses-----")
    for i,e in enumerate(expenses,start=1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['desc']} | {e['date']}")

def category_summary(expenses):
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat,0) + e["amount"]
    print("\n----category summary----")
    for cat,amt in summary.items():
        print(f"{cat}:₹{amt}")

def save_expenses(expenses,filename ="expenses.json"):
    try:
        with open(filename,"w") as f:
            json.dump(expenses,f,indent=4)
        print("expenses saved successfully!")
    except Exception as e:
        print("Error saving expenses:",e)

def load_expenses(filename ="expenses.json"):
    try:
        with open(filename,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error loading expenses:",e)
        return []

def set_budget():
    try:
        budget = float(input("enter the budget:$"))
        if budget < 0:
            print("buget cannot be zero")
            return None
        print(f"monthly budget set to {budget}")
        return budget
    except ValueError:
        print("invalid number!")
        return None

def calculate_total(expenses):
    total = 0
    for e in expenses:
        total+=e["amount"]
    return total
        
def check_budget_warning(expenses,budget):
    if budget is None:
        return
    total_spent = calculate_total(expenses) 
    percent = (total_spent/budget *100)
    print(f"total spent:{total_spent}/{budget}")

    if percent >= 100:
        print("budget exceeded!")
    elif percent >=80:
        print(f"u have used {budget}% of budget")               
             
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
            print("Goodbye!")
            break
