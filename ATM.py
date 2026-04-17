def show_balance():
    print(f"Your balance is ₹{balance:.2f}")
    
def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
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
        return amount

balance = 0
is_running = True

while is_running:
    print("**************************************")
    print("   Banking Program   ")
    print("**************************************")
    print("   1. Show Balance   ")

    print("   2. Deposit        ")
    
    print("   3. Withdraw       ")
    
    print("   4. Exit           ")

    choice = input("Enter your choice (1-4): ")
    print("**************************************")

    if choice == "1":
            show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdrawal()
    elif choice == "4":
        is_running = False
    else:
        print("That is not a valid choice")

print("Thank you, have a nice day!")