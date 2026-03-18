def view_expenses(expenses):
    if not expenses:
        print("no expenses recorded")
        return
    print("\n-----All Expenses-----")
    for i,e in enumerate(expenses,start=1):
        print(f"{i}. ₹{e['amount']} | {e['category']} | {e['desc']} | {e['date']}")
