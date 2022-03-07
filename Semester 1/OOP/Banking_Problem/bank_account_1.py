import functions

accounts = {}
with open("accounts.csv", 'r') as f: file = f.read()
file2 = open('accounts.csv', 'w')
data = file.split("\n")
test = []
for i in range(len(data)):
    try:
        test = data[i].split(',')
        accounts.update({test[0]: int(test[1])})
    except IndexError: pass

def append_accounts():
    a = ''
    for i in accounts.items():
        a += i[0] + ',' + str(i[1]) + "\n"
    file2.write(a)
    exit()

def main():
    print("=== Welcome to National Bank ===")
    while True:
        try:
            acc = functions.Account()
            user_input = input("\nEnter your name: ")
            user_input = user_input.lower().strip()
            while True:
                if user_input in accounts.keys():
                    while True:
                        select = functions.choice_1(user_input)
                        if select == 1 or select == 2:
                            if select == 1:
                                while True:
                                    usr_choice = functions.choice_2()
                                    if usr_choice == 1 or usr_choice == 2 or usr_choice == 3:
                                        if usr_choice == 1:
                                            if user_input.lower().strip() not in accounts:
                                                accounts.update({user_input:0})
                                            print(f'{user_input.upper()}\'s current balance is: Rp {accounts.get(user_input)}')
                                            user_input3 = int(input("\nHow many do you want to deposit? Rp "))
                                            accounts.update({user_input:accounts.get(user_input)+user_input3})
                                            print(f'{user_input.upper()}\'s current balance is: Rp {accounts.get(user_input)}. Thank you for using our service.\n')
                                        if usr_choice == 2:
                                            if user_input.lower().strip() not in accounts:
                                                accounts.update({user_input: 0})
                                            while True:
                                                print(f'{user_input.upper()}\'s current balance is: Rp {accounts.get(user_input)}')
                                                user_input3 = int(input("\nHow many do you want to withdraw? Rp "))
                                                if user_input3 > accounts.get(user_input):
                                                    print("\nError! Your input exceeded the current balance: "+str(accounts.get(user_input)))
                                                else:
                                                    accounts.update({user_input:accounts.get(user_input)-user_input3})
                                                    print(f'\n{user_input.upper()}\'s current balance is: Rp {accounts.get(user_input)}. Thank you for using our service.\n')
                                                    break
                                        if usr_choice == 3:
                                            if user_input.lower().strip() not in accounts:
                                                accounts.update({user_input: 0})
                                            print(f'{user_input.upper()}\'s current balance is: Rp {accounts.get(user_input)}')
                                        while True:
                                            state = functions.terminate()
                                            if state == 1:
                                                break
                                            if state == 2:
                                                print("\nThank you for using our service.")
                                                append_accounts()
                                            elif state < 1 or state > 2:
                                                print("\nInvalid input! Try again\n")
                                    else: print("\nInvalid input! Try again")
                            if select == 2:
                                while True:
                                    user_input = input("\nEnter your name: ")
                                    user_input = user_input.lower().strip()
                                    if user_input in accounts:
                                        break
                                    else:
                                        print("\nSuccess! Account has been created.")
                                        break
                        else: print("\nInvalid input. Try again")
                else:
                    print(f'\nSuccess! Account has been created.\n\n{user_input.upper()}\'s current balance is: Rp {acc.get_balance()}')
                    user_input3 = int(input("How many do you want to deposit? Rp "))
                    acc.deposit(user_input3)
                    print(f'\n{user_input.upper()}\'s current balance is: Rp {acc.get_balance()}\n')
                    accounts.update({user_input : acc.get_balance()})
                    while True:
                        state = functions.terminate()
                        if state == 1:
                            break
                        elif state == 2:
                            print("\nThank you for using our service.\n === National Bank ===")
                            a = ''
                            for i in accounts.items():
                                a += i[0] + ',' +str(i[1]) + "\n"
                            file2.write(a)
                            exit()
                        elif state < 1 or state > 2:
                            print("\nInvalid input! Try again\n")
        except ValueError:
            print("\nSomething unexpected happened. Program has been terminated to prevent data corruption.\n === National Bank ===")
            append_accounts()
main()