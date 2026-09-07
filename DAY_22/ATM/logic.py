data = {
    123456: {'name': 'Lohitha', 'pin': 1234, 'balance': 5000, 'history': []},
    234561: {'name': 'Harsha', 'pin': 1234, 'balance': 4000, 'history': []},
    345621: {'name': 'Avinash', 'pin': 1234, 'balance': 2500, 'history': []},
    456123: {'name': 'Sree', 'pin': 1234, 'balance': 500, 'history': []}
}


def login():
    global acc_num

    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))

    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True
    else:
        print("Invalid Login")
        return False


def menu():
    print(f"\nWelcome to the ATM, {data[acc_num]['name']}")
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew Transaction")
    print("[E]xit")


def checkbalance():
    print(f"\nHello {data[acc_num]['name']},")
    print("Current balance:", data[acc_num]["balance"], end="\n\n")


def deposit():
    amount = int(input("Enter the amount to deposit: "))

    if amount > 0:
        data[acc_num]['balance'] += amount
        data[acc_num]['history'].append(f"{amount} is deposited")
        print(f"{amount} is deposited successfully")
        checkbalance()
    else:
        print("Enter a valid amount")


def withdraw():
    amount = int(input("Enter the amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -= amount
        data[acc_num]["history"].append(f"{amount} is withdrawn")
        print(f"{amount} is withdrawn successfully")
        checkbalance()

    else:
        print("Insufficient Balance")


def viewtransaction():
    if data[acc_num]["history"]:
        print("\n-------- Transaction History --------")

        for i in data[acc_num]["history"]:
            print(i)

        print("-------- End of History --------")

    else:
        print("No Transaction History")


