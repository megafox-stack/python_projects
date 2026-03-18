import json
import os

def save_accounts(accounts, filename=None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "accounts.json")
    try:
        with open(filename,"w") as f:
            json.dump(accounts,f,indent = 4)
        print("account details saved successfully!")
    except Exception as e:
        print("error saving accounts",e)

def load_account(filename = None):
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), "accounts.json")
    try:
        with open(filename,"r") as f:
            data = json.load(f)
        accounts = {int(k):v for k,v in data.items()}
        return accounts
    except FileNotFoundError:
        return {}