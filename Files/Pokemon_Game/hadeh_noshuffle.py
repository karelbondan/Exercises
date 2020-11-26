import random

with open("pokemon.txt", 'r') as f:
    file = f.read()
data = file.split(' ')

def game():
    pokemons = []
    curr = ""
    count = 0
    while count<=100:
        a = random.choice(data)
        if count == 0:
            curr += a
            pokemons.append(a)
            count += 1
        else:
            for i in range(len(data)):
                if data[i][0] == curr[-1]:
                    if data[i] in pokemons:
                        continue
                    else:
                        pokemons.append(data[i])
                        curr = ""
                        curr += pokemons[-1]
                        break
                else:
                    continue
        count += 1
    return pokemons