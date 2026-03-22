def calculate_total(expenses):
    total = 0
    for e in expenses:
        total+=e["amount"]
    return total