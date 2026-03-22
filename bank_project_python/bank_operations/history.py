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