num_1 = int(input("enter the num_1: "))
num_2 = int(input("enter the num_2: "))
print(num_1+num_2)
print(num_1-num_2)
try:
    print(num_1/num_2)
except:
    print(f"error occured")
print(num_1+num_2)
print(num_1-num_2)

balance = 0
mini_statement = []

def credit():
    global balance
    try:

        amount = float(input("Enter amount to credit:"))

        if amount <= 0:
            print("please enter a postive amount.")

        else:
            balance += amount
            mini_statement.append(f"credited: $ {amount}")
            print(f"${amount} credited to your account.")

    except:
        print(f"enter numerics postive numerics")
       


def debit():
    global balance
    try:

        amount = float(input("Enter amount to debit:"))

        if amount > balance:
            print("insufficient balance.")

        else:
            balance -= amount
            mimi_statement.append(f"debited: $ {amount}")
            print(f"${amount} debited from your account.")
    except:
        print(f"error occured enter postive numerics")

def check_balance():
    print(f"your account balance is: $ {balance}")

def menu():
    while True:

        print("\nATM MENU:")
        print("1. Credit")
        print("2. Debit")
        print("3. Balance")
        print("4. Mini Statement ")
        print("5. Exit")

        choice = input("Enter your choice (1_5): ")

        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            show_mini_statement()

        elif choice == '5':
            print("thank you for using the ATM. Goodbye!")
            break

        else:
            print("invalid choice. please try again.")


# function calling
menu()



