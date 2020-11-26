import random

with open("pokemon.txt", 'r') as f:
    file = f.read()

seq = []
bla = 0
longest_seq = 0
data = file.split(' ')

#def counting(idklol):
    #print(len(idklol))
    #global bla
    #seq.append(idklol)
    #longest_seq = 0
    #while bla <= 1:
        #bla += 1
        #game()
    #for i in seq:
        #if len(i) > longest_seq:
            #longest_seq = len(i)
    #return longest_seq

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
                        random.shuffle(data)
                        curr = ""
                        curr += pokemons[-1]
                        break
                else:
                    continue
        count += 1
    return pokemons