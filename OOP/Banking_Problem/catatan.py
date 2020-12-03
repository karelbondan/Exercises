import string

class Account:
    def __init__(self, balance=1000):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:

            return False


class Customer(Account):
    firstname = None
    lastname = None

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def set_account(self):
        return f'Your initial balance is Rp {Account().get_balance()}'

    def get_account(self):
        return f'Your current balance is Rp {Account().get_balance()}'


class Bank:
    def __str__(self):
        return "National Bank"

    def add_customer(self, firstname: str, lastname: str):
        Customer.firstname = firstname
        Customer.lastname = lastname


def choice_1_account():
    selection = int(input("What do you want to do?\n"
                          "1. Register new account\n"
                          "2. Access existing account\n"
                          "Your input: "))
    return selection

def choice_2_accexist():
    selection = int(input("Account already exist. Do you want to access that account?\n"
                          "1. Yes\n"
                          "2. No\n"
                          "Your input: "))
    return selection

def choice_3_accoptions():
    selection = int(input("What do you want to do?\n"
                            "1. Deposit\n"
                            "2. Withdraw\n"
                            "3. Balance Inquiry\n"
                            "Select the option by typing the number: "))
    return selection


def choice_4_pin_exit():
    selection = int(input("\n1. Enter pin\n"
                          "2. Exit\n"
                          "Select the option by typing the number: "))
    return selection

def name_error(name):
    counter = 0
    for i in name:
        if i in string.punctuation or i in string.digits:
            print("\nInvalid name. Please enter a valid name.")
            counter += 1
        else: pass
    return counter


def pin_error(pin):
    counter = 0
    for i in pin:
        if i in string.ascii_letters or i in string.punctuation:
            print("\nInvalid pin. Please try again.")
            counter += 1
        else: pass
    return counter



"""
class aAccount:
    #class variable
    no_of_account = 0
    def __init__(self, balance = 1000):
        self.balance = balance #instance variable

new_account = aAccount()
print(new_account.balance)
another_account = aAccount(50000)
print(another_account.balance)

def main():
    account = Account()
    print(account.get_balance())
    if account.deposit(2000):
        print("balance updated,",account.get_balance())
    else:
        print("invalid transaction, balance is not updated;",account.get_balance())
    if account.withdraw(100000):
        print("balance updated,",account.get_balance())
    else:
        print("invalid transaction, balance is not updated;",account.get_balance())

if __name__ == "__main__":
    main()

Homework
    1. menu driven program that can:
        a. add account
        b. deposit
        c. withdraw
        d. balance inquiry
        e. quit
"""
