import logic as lg

if lg.login():
    while True:
        lg.menu()
        ch = input("Enter the choice: ").upper()
        if ch == 'C':
            lg.checkbalance()
        elif ch == 'D':
            lg.deposit()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'V':
            lg.viewtransaction()
        elif ch == 'E':
            print("-----------------Thank you, Visit Again-----------------")
            break
        else:
            print("Enter the valid choice")                
