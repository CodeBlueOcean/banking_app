def show_balance(balance):
    print("Your Balance is: ", float(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    total = amount + balance
    balance += total 
    return float(balance)

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    total = amount + balance
    balance -= total 
    return float(balance)

def logout(name):
    print("Goodbye", name)

