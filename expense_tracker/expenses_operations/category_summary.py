def category_summary(expenses):
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat,0) + e["amount"]
    print("\n----category summary----")
    for cat,amt in summary.items():
        print(f"{cat}:₹{amt}")