import json

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