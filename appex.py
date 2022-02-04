def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

name = input("Enter name to register:")
pin = input("Enter PIN:")
balance = 0
print(name,"has been registered with a starting balance of $", float(balance))

while True:
    print("          === Automated Teller Machine ===          ")
    name_to_validate = input("Enter Name:")
    pin_to_validate = input("Enter PIN:")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login sucessful!")
        break
    else: 
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = int(input("Choose an option:"))

    if option == 1:
        print("Your Balance is: ", balance)
        anothertrans = input("Do you want to make another transaction yes/no: ")
        if anothertrans == "yes": 
            continue
        else: 
            break
    elif option == 2:
        deposit = float(input("Enter amount to deposit"))
        totalbalance = balance + deposit
        print("success")
        print("total balance now is: ", totalbalance)    
    elif option == 3:
        withdraw = float(input("Enter amount to withdraw"))
        if totalbalance > withdraw:
            totalbalance = totalbalance - withdraw
            print("Success")
            print("Your new balance is", totalbalance)
        else: 
            print("insufficient balance")     
    elif option == 4:
        print("closing the program...")
        exit() 
        break
    else:
        print("No selected transaction")
