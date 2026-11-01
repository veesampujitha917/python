balance = 5000.0

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        if amount > 0:
            balance += amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 3:
        try:
            amount = float(input("Enter withdrawal amount: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")