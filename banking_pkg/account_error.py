def show_balance(balance):
    print("The current balance is: $"+str(balance))
     
def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return balance + float(amount)

def widthdraw(balance):
    amount = input("Enter amount to withdraw: $")
    if amount > balance:
        print("Where are you going to get that kind of money")
        return balance - float(amount)

    
def logout(name):
    print("Goodbye", name + "!")



