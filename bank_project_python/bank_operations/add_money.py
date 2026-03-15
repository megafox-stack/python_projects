from bank_project_python.bank_operations.saveandload import save_accounts

def add_money(accounts, account):
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