import string

class Bank:
    numberOfCustomers = 0

    def __init__(self, bankname, customers):
        self.bankname = bankname
        self.customers = customers

    def add_customer(self, f, l):
        self.customers.append(Customer(f, l))
        self.numberOfCustomers += 1

    def get_number_of_customers(self):
        return self.numberOfCustomers

    def get_customer(self, index):
        return self.customers[index]


class Customer:
    def __init__(self, f, l):
        self.firstName = f
        self.lastName = l
        self.account = Account()

    def get_fname(self):
        return self.firstName

    def get_lname(self):
        return self.lastName

    def get_account(self):
        return self.account

    def set_account(self, acc):
        self.account = acc


class Account:
    # class variable
    noOfAccounts = 0

    def __init__(self, balance=1000):
        self.balance = balance  # instance variable

    def get_balance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance and amt > 0:
            self.balance = self.balance - amt
            return True
        else:
            return False

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
    if len(name) == 0:
        print("Name cannot be empty")
        counter += 1
    return counter


def pin_error(pin):
    counter = 0
    for i in pin:
        if i in string.ascii_letters or i in string.punctuation:
            print("\nInvalid pin. Please try again.")
            counter += 1
        else: pass
    if len(pin) != 6:
        print("Your pin must be 6 digits long. Please try again.")
        counter += 1
    return counter
