from bank_project_python.bank_operations.saveandload import save_accounts
from bank_project_python.bank_operations.confirmpin import confirm_pin

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
