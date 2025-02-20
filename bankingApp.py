class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"{amount} deposited successfully!")
        else:
            print("Deposit amount must be greater than zero.")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrawn: {amount}")
                print(f"{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be greater than zero.")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")
    

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_holder):
        if account_holder not in self.accounts:
            new_account = BankAccount(account_holder)
            self.accounts[account_holder] = new_account
            print(f"Account created successfully for {account_holder}.")
        else:
            print("Account already exists.")
    
    def get_account(self, account_holder):
        return self.accounts.get(account_holder, None)

def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Banking Management System")
        print("1. Create a new account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")
        
        choice = input("Please choose an option (1-5): ")
        
        if choice == '1':
            account_holder = input("Enter the account holder's name: ")
            bank.create_account(account_holder)
        
        elif choice == '2':
            account_holder = input("Enter the account holder's name: ")
            account = bank.get_account(account_holder)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found!")
        
        elif choice == '3':
            account_holder = input("Enter the account holder's name: ")
            account = bank.get_account(account_holder)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found!")
        
        elif choice == '4':
            account_holder = input("Enter the account holder's name: ")
            account = bank.get_account(account_holder)
            if account:
                account.check_balance()
            else:
                print("Account not found!") 
        
        elif choice == '5':
            print("Thank you for using the Banking Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
