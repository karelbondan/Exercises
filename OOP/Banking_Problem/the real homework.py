import catatan

acc = catatan
accounts = {}
with open("accounts_3.csv", 'r') as f: file = f.read()
file2 = open('accounts_3.csv', 'w')
data = file.split("\n")
test = []
passbal = []
for i in range(len(data)):
    try:
        test = data[i].split(',')
        passbal.extend((test[1], test[2]))
        accounts.update({test[0]: passbal})
        passbal = []
    except IndexError:
        pass

def append_accounts():
    a = ''
    for i in accounts.items():
        a += f'{i[0]},{i[1][0]},{i[1][1]}\n'
    file2.write(a)
    exit()

def main():
    customers = []
    pepepopo = acc.Bank("BCA", customers)
    name = ""
    print("\n=== Welcome to The National Bank of PeePeePooPoo ===\n")
    while True:
        try:
            input_1 = acc.choice_1_account()
            if input_1 == 1:
                while True:
                    print("\nPlease enter your legal name based on your Identity Card")
                    firstname = input("First name: ").strip().upper()
                    firstname_check = acc.name_error(firstname)
                    if firstname_check == 0: break
                    else: pass
                while True:
                    lastname = input("Last name: ").strip().upper()
                    lastname_check = acc.name_error(lastname)
                    if lastname_check == 0: break
                    else: pass
                name += f'{firstname} {lastname}'
                if name in accounts.keys():
                    print("Account already exist.")
                    access_account(firstname, lastname)
                else:
                    while True:
                        pin = input("Set a pin (digits only): ")
                        pin_check = acc.pin_error(pin)
                        if pin_check == 0: break
                        else: pass
                    pepepopo.add_customer(firstname, lastname.upper())
                    print(f'\n- Registration Completed -\n'
                          f'Welcome to National Bank of PeePeePooPoo, {pepepopo.get_customer(0).get_fname()} {pepepopo.get_customer(0).get_lname()}')
                    input_2 = int(input(f'Your initial balance is Rp {pepepopo.get_customer(0).get_account().get_balance()}, How many do you want to deposit?\n'
                                        f'Amount: Rp '))
                    pepepopo.get_customer(0).get_account().deposit(input_2)
                    print(f'\nThe balance for {name}\'s account is now Rp {pepepopo.get_customer(0).get_account().get_balance()}. Thank you for using our Service.\n=== PeePeePooPoo National Bank ===')
                    passbal.extend((pin, pepepopo.get_customer(0).get_account().get_balance()))
                    accounts.update({name: passbal})
                    append_accounts()
                break
            elif input_1 == 2:
                name = ''
                counter = 0
                while True:
                    print("\nEnter your full name")
                    first_name = input("First name: ").strip().upper()
                    last_name = input("Last name: ").strip().upper()
                    name += f'{first_name} {last_name}'
                    if name in accounts.keys(): access_account(first_name, last_name)
                    else:
                        print("\nAccount not found. Please try again.")
                        name = ''
                        counter += 1
                    if counter == 5:
                        print("\nToo many failed attemps. Program has been terminated.\n=== PeePeePooPoo National Bank ===")
                        append_accounts()
            else:
                print("\nInvalid input. Please enter a number that corresponds to the menu.\n")
        except ValueError:
            print("\nSomething unexpected happened. Program has been terminated to prevent data corruption.\n=== PeePeePooPoo National Bank ===")
            append_accounts()

def access_account(firstname='default', lastname='default'):
    name = ''
    name += f'{firstname} {lastname}'
    existing_account = acc.Account(int(accounts.get(name)[1]))
    try:
        if firstname != 'default' and lastname != 'default':
            while True:
                input_7 = acc.choice_4_pin_exit()
                if input_7 == 1:
                    while True:
                        input_4 = int(input("\nEnter your pin (digits): "))
                        if input_4 == int(accounts.get(name)[0]):
                            print(f'\nHowdy, {name}')
                            input_5 = acc.choice_3_accoptions()
                            if input_5 == 1:
                                while True:
                                    input_6 = int(input("Your amount of money: Rp "))
                                    if existing_account.deposit(input_6) == True:
                                        print(f'\nYour balance is now Rp {existing_account.get_balance()}')
                                        break
                                    else: print("Are you joking or something? There's no such thing as a negative amount of money.")
                            elif input_5 == 2:
                                while True:
                                    input_6 = int(input("Your amount of money: Rp "))
                                    if existing_account.withdraw(input_6) == True:
                                        print(f'\nYour balance is now Rp {existing_account.get_balance()}')
                                        break
                                    else: print("Your entered amount exceeded your current balance/you probably entered a negative amount. Bruh.")
                            elif input_5 == 3:
                                print(f'\n{name}\'s balance is Rp {existing_account.get_balance()}')
                                break
                            else: print("Invalid input. Please enter a number that corresponds to the menu.")
                        else: print("Wrong pin. Try again.")
                        break
                elif input_7 == 2:
                    print("\nThank you for using our service.\n=== PeePeePooPoo National Bank===")
                    break
                else: print("Invalid input. Please enter a number that corresponds to the menu.")
            passbal.extend((accounts.get(name)[0], existing_account.get_balance()))
            accounts.update({name:passbal})
            append_accounts()
        else: pass
    except ValueError:
        print("\nProgram error. Your balance did not change.")
        print("Something unexpected happened. Program has been terminated to prevent data corruption.\n=== PeePeePooPoo National Bank ===")
        append_accounts()
main()
