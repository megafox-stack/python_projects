from bank_project_python.bank_operations.saveandload import save_accounts
def withdraw_money(accounts, account):
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
