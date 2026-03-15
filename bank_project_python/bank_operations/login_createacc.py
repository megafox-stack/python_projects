from bank_project_python.bank_operations.saveandload import save_accounts
def create_account(accounts, next_account_number):
    name = input("enter ur name:").strip('"')
    if not name:
        print("name cannot be empty")
        return next_account_number
    pin = (input("set a 4 digit pin:")).strip()
    if not pin.isdigit() or len(pin)!=4:
        print("pin should be 4 digits")
        return next_account_number
    account = {"account_no":next_account_number,
               "name":name,
               "balance":0, 
               "transactions":[],
               "pin":pin
               }
    accounts[next_account_number] = account
    print(f"u have successfully opened an account:{next_account_number}")
    next_account_number += 1
    save_accounts(accounts)
    return next_account_number

def login(accounts):
    try:
        account_number = int(input("enter ur account number:"))
    except ValueError:
        print("invalid account number!")
        return None

    if account_number not in accounts:
        print("account not found")
        return None
            
    for _ in range(3):
        pin = (input("enter pin:")).strip()
        if pin == accounts[account_number]["pin"]:  
            print(f"Welcome {accounts[account_number]['name']}")
            return account_number
        else:
            print("invalid pin!")

    print("too many attemps.account locked temporarily")
    return None        

