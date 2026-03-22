from .total_expenses import calculate_total
def set_budget():
    try:
        budget = float(input("enter the budget:$"))
        if budget <= 0:
            print("budget cannot be zero or negative")
            return None
        print(f"monthly budget set to {budget}")
        return budget
    except ValueError:
        print("invalid number!")
        return None
    
def check_budget_warning(expenses,budget):
    if budget is None:
        return
    total_spent = calculate_total(expenses) 
    percent = (total_spent/budget *100)
    print(f"total spent:{total_spent}/{budget}")

    if percent >= 100:
        print("budget exceeded!")
    elif percent >= 80:
        print(f"you have used {percent:.1f}% of budget")    