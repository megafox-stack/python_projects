
from bank_project_python.bank_operations.saveandload import save_accounts,load_account
from bank_project_python.bank_operations.login_createacc import create_account,login
from bank_project_python.bank_operations.add_money import add_money
from bank_project_python.bank_operations.withdraw_money import withdraw_money
from bank_project_python.bank_operations.balance import balance_account
from bank_project_python.bank_operations.history import show_history
from bank_project_python.bank_operations.transfer_money import transfer_menu

next_account_number = 1001
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
            next_account_number = create_account(accounts, next_account_number)

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
                    add_money(accounts, account)
                elif option == 3:
                    withdraw_money(accounts, account)
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
                    
                    

    
            
            


