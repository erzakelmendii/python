print('- ATM Transaction - ')
print('=' * 30)
print("""
1 - Terheqje
2 - Bilanci
3 - Deponim
""")
pin_from_db = "123456"
account_balance = 1500.00

while True:
    user_pin = input("Type your PIN? ")
    if pin_from_db == user_pin:
        print("Welcome to ATM")
        print()
        break
    else:
        print("You typed wrong PIN!")

while True:
    option = int(input("What do you want to do?"))
    if option == 1:
        value = float(input("Type your amont for withdraw? "))
        if value <= account_balance:
            account_balance = account_balance - value
            print("Your transaction was successfully?")
            print(f'Your new balance is: {account_balance}\n')
        else:
            print("Your Balance is suficient!")
            print("Transaction was not completed!\n")
    elif option == 2:
        print(f"Your balance is: {account_balance}\n")
    elif option == 3:
        value = float(input("Type your amount? "))
        account_balance = account_balance + value
        print(f'Your new balance is: {account_balance}\n')
    elif option == 100:
        print("Thank you!")
        break
