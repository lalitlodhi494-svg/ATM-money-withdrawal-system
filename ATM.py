# Simple mobile  moneybanking program in Python
history = []
is_running = True
balance = 0

def show_balance(amount):

    if amount > 0:
         print(f" 👉 Your balance is ₹{balance:.2f}")  
    else:
        print(f" 👉 Your balance is (₹{balance:.2f}) You need to deposit to see the balance.")
    return 0
     
def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        history.append(f" 👉 Deposited ₹{amount:.2f}")
        return amount

def withdrawal():
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("You do not have enough funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        history.append(f" 👉 Withdrew ₹{amount:.2f}")
        return amount

def transaction():
    if not history:
        print("No transactions yet.")
    else:
        print("\nTransaction History:")
        for item in history:
            print("-", item)

def help():
    print("This is a simple banking program that allows you to check your balance, \ndeposit money, and withdraw money.\n")

    print("To use the program, simply enter the number corresponding to the action you want to perform.\n")
    
    print("For example, to check your balance, enter'1'.\n To deposit money, enter'2'.\nTo withdraw money, enter'3'.\n to View transaction history. \n for exit press '5'.")


while is_running:
    print("**************************************")
    print("   Mobile Banking Program   ")
    print("**************************************")
    print("   1. Show Balance   ")

    print("   2. Deposit        ")
    
    print("   3. Withdraw       ")

    print("   4. View transaction history") 
    
    print("   5. Exit           ")

    print("   6. Help           ")

    

    choice = input("Enter your choice (1-6): ")
    print("**************************************")

    if choice == "1":
            show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdrawal()
    elif choice == "4":
           transaction ()
    elif choice == "5":
           exit ()     
    elif choice == "6":
        help ()
        is_running = False 
    else:
        print("That is not a valid choice")

print("Thank you, have a nice day!")
