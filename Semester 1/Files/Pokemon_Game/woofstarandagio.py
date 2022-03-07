import random

with open("pokemon.txt", 'r') as f:
    file = f.read()

def game():
    pokemons = []
    curr = ""
    data = file.split(' ')
    random.shuffle(data)
    count = 0
    woofstar = 0
    dagio = 0
    print("\nOne day, in a realm far away from the world of the living...\n")
    print('Woofstar: "Hey Dagio, wanna play a game?"')
    print('Dagio: "Sure, why not."')
    print('Woofstar: "Ok so, I\'m gonna say a pokemon name. You\'ll have to say the next one whose name starts with the last letter of the pokemon I\'ve just said. Got it?"')
    print('Dagio: "Alright. The same goes for you right?"')
    while len(data) > 0:
        a = random.choice(data)
        if count == 0:
            curr += a
            print('Woofstar: "Yep. Now, here goes. '+curr.capitalize()+'!"')
            count += 1
        else:
            for i in range(len(data)):
                if data[i][0] == curr[-1]:
                    pokemons.append(data[i])
                    data.pop(i)
                    curr = ""
                    curr += pokemons[-1]
                    print('Dagio: "'+pokemons[-1].capitalize()+'!"')
                    dagio += 1
                    break
                else: continue
            for i in range(len(data)):
                if data[i][0] == curr[-1]:
                    pokemons.append(data[i])
                    data.pop(i)
                    curr = ""
                    curr += pokemons[-1]
                    print('Woofstar: "'+pokemons[-1].capitalize()+'!"')
                    woofstar += 1
                    break
                else: continue
        count += 1
        if count == 1000:
            if dagio > woofstar:
                print('Woofstar: "Tch, you\'re good. This is not the last of me!"')
                print('Dagio: "Jejeje... whatever you say, detective."')
            else:
                print('Dagio: "Whew you\'re good. Nothing in my mind anymore."')
                print('Woofstar: "Hell yeah!"')
            print("\nThe end")
            break
game()