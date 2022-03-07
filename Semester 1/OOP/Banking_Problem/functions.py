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


def terminate():
    user_input = int(input("What do you want to do?\n"
                           "1. Do something else\n"
                           "2. Quit\n"
                           "Select the option by typing the number: "))
    return user_input


def choice_1(user_input):
    select = int(input(
        "\nAn account with the name " + str(
            user_input.upper()) + " exists. Do you want to access or register a different account?\n"
                                  "1. Access account\n"
                                  "2. Register a different account\n"
                                  "Select the option by typing the number: "))
    return select


def choice_2():
    user_input2 = int(input("\nWhat do you want to do?\n"
                            "1. Deposit\n"
                            "2. Withdraw\n"
                            "3. Balance Inquiry"
                            "Select the option by typing the number: "))
    return user_input2
