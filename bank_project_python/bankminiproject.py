import json
next_account_number = 1001

def create_account(accounts):
    global next_account_number
    name = input("enter ur name:").strip('"')
    if not name:
        print("name cannot be empty")
        return
    pin = (input("set a 4 digit pin:")).strip()
    if not pin.isdigit() or len(pin)!=4:
        print("pin should be 4 digits")
        return 
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


def balance_account(account):
    print(f"your current balance:$",account["balance"])
    return account["balance"]


def add_money(account):
    try:
        deposit = int(input("how much u want to deposit:$"))
    except ValueError:
        print("invalid input!")    
        
    if(deposit <= 0):
        print("u cant add negative money")
        return

    account["balance"] += deposit
    account["transactions"].append({"type":"deposit","amount":deposit})
    print("money added sucessfully")
    save_accounts(accounts)    


def withdraw_money(account):
    try:
        withdraw = int(input("how much to withdraw:$"))
    except ValueError:
        print("invalid input!")
        return None

    if withdraw <= 0:
        print("insuffiecent balance")
        return
         
    if withdraw > account["balance"]:
      print("ur bankrupt!plz add money")
      return 

    account["balance"]-= withdraw
    account["transactions"].append({"type":"withdraw","amount":withdraw})

    print("withdraw successfull!")
    save_accounts(accounts)    


def show_history(account):
   if not account["transactions"]:
      print("no history")
      return
    
   print("transaction history:")
   for i, t in enumerate(account["transactions"], start=1):
        line = f"{i}. {t['type']} - ${t['amount']}"

        if "to" in t:
            line += f" → to account {t['to']}"
        if "from" in t:
            line += f" ← from account {t['from']}"

        print(line)
   

def transfer_money(accounts,from_accounts,to_account,amount):
    
    if from_accounts not in accounts:
        print("sender account not found!")
        return False
    
    if to_account not in accounts:
        print("reciever account not found!")
        return False
    
    if from_accounts == to_account:
        print("cannot trasfer to same account")
        return False
    
    if accounts[from_accounts]["balance"] < amount:
        print("insufficient balance.")
        return False
    accounts[from_accounts]["balance"]-=amount
    accounts[to_account]["balance"]+=amount

    accounts[from_accounts]["transactions"].append({
        "type": "TRANSFER OUT",
        "amount": amount,
        "to": to_account
    })
    accounts[to_account]["transactions"].append({
        "type": "TRANSFER IN",
        "amount": amount,
        "from": from_accounts})

    print("transfer successfull!")
    return True

def confirm_pin(account):
    for _ in range(3):
        pin = input("Confirm pin:").strip()
        if pin == account["pin"]:
            return True
        else:
            print("incorrect pin")
    print("too many wrong attemps!try again later")
    return False
         


def transfer_menu(accounts,current_account):
    try:
        to_account = int(input("enter reciever account number:"))
        amount = int(input("enter the amount to trasfer:$"))

        if amount <= 0:
            print("invalid amount")
            return
        
        if to_account == current_account:
         print("cannot trasfer to ur own account!")
         return 
        
        account = accounts[current_account]
        if not confirm_pin(account):
            return

        transfer_money(accounts,current_account,to_account,amount) 
    
    except ValueError:
        print("invalid input")
    save_accounts(accounts)    

def save_accounts(accounts,filename="accounts.json"):
    try:
        with open(filename,"w") as f:
            json.dump(accounts,f,indent = 4)
        print("account details saved successfully!")
    except Exception as e:
        print("error saving accounts",e)

def load_account(filename = "accounts.json"):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
        accounts = {int(k):v for k,v in data.items()}
        return accounts
    except FileNotFoundError:
        return {}
            
         

if __name__ == "__main__":
    accounts = load_account()

    if accounts:
        next_account_number = max(accounts.keys()) + 1
    else:
        next_account_number = 1001    
   
    while True:
        print("welcome to python bank!")
        print("\n1 Create account")
        print("2 Login")
        print("3 Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            create_account(accounts)

        elif choice == 2:
            account_number = login(accounts)
            if account_number is None:
                continue
         

            account = accounts[account_number]

           
            while True:
                print("\n1 Balance  2 Deposit  3 Withdraw  4 History  5 Transfer 6 Exit")
                option = int(input("Choose: "))

                if option == 1:
                    balance_account(account)
                elif option == 2:
                    add_money(account)
                elif option == 3:
                    withdraw_money(account)
                elif option == 4:
                    show_history(account)
                elif option == 5:
                    transfer_menu(accounts,account_number)
                else:
                    print("logged out")
                    break
        else:
              print("exiting the bank....")
              break          
                    
                    

    
            
            


