# 1. A BankAccount class with:
# account_number
# account_holder
# balance

# 2. Methods inside the class:
# deposit(amount) → add money to balance.
# withdraw(amount) → subtract money (only if balance is enough).
# check_balance() → return the current balance.

# 3.A small menu system in the main program that allows the user to:
# Create an account.
# Deposit money.
# Withdraw money.
# Check balance.
# Exit.

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number 
        self.balance = balance
    
    def __repr__(self):
        return f"\n User: {self.account_holder} \n Details: {self.account_number} \n Account balance is: {self.balance}"

class Transaction:

    def __init__(self):
        self.Acct_Details = []


    def Create(self):
        print("do you want to create an account? ")
        user_input = input("y/n: ").lower()
        if user_input == "y":
            account_holder = input("what is your name: ")
            account_number = input("what is your phone details: ")
            balance_input = int(input("Make a deposit or leave your account empty: "))
            balance = int(balance_input) if balance_input else 0

            print("Please note that your account_number will be your phone details")
            if account_holder != "":
                details = BankAccount(account_holder, account_number, balance) 
                self.Acct_Details.append(details)
                print(f"Dear {account_holder} your account number is {account_number} and current balance is {balance}")
                for acc in self.Acct_Details:
                    print(acc)

            else:
                pass

        else:
            print("Thank you for using this app")

    def Deposit(self):
        acct_num = input("input your account number: ")
        for acc in self.Acct_Details:
            if acc.account_number == acct_num:
                amount_input = input("how much do you want to deposit: ")
                amount = int(amount_input)
                if amount >= 0 :
                    acc.balance += amount 
                    print(f"Deposit Successful: Your current balance is {acc.balance}")
                    return
        print("Account not found")

        
    def Withdraw(self):
        acct_num = input("input your account number: ")
        for acc in self.Acct_Details:
            if acc.account_number == acct_num:
                amount_withdraw = input("how much do you want to withdraw: ")
                amount = int(amount_withdraw)
                if amount <= 0 :
                    print("please enter a number greater than 0")
                elif amount > acc.balance:
                    print("Insufficient Funds")
                else:
                    acc.balance -= amount 
                    print(f"Withdrawal Successful: Your Current balance is {acc.balance}")

        
    def Balance(self):
        
        acct_num = input("input your account number: ")
        found = False
        for acc in self.Acct_Details:
            if acc.account_number == acct_num:
                print(f"Kindly find your available balance: {acc.balance}")
                found = True
                break

        if not found:
            print("Account doesn't exist")


def main():

    A = Transaction()
    print("Welcome to your favorite bank app")
    print("1. Create an Account")
    print("2. Make a Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    while True:
        holder = input("Kindly press a number: ")
        if holder == "1":
            A.Create()
        elif holder == "2":
            A.Deposit()
        elif holder == "3":
            A.Withdraw()
        elif holder == "4":
            A.Balance()
        elif holder == "5":
            print("See you next time")
            break
        else:
            print("please enter a number between 1 and 5")


main()