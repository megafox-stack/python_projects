def confirm_pin(account):
    for _ in range(3):
        pin = input("Confirm pin:").strip()
        if pin == account["pin"]:
            return True
        else:
            print("incorrect pin")
    print("too many wrong attemps!try again later")
    return False