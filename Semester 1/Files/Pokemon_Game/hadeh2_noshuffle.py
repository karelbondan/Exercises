import hadeh_noshuffle as h

count = 0
length = []
sequences = []
while count <= 300:
    count += 1
    test = h.game()
    if test != None:
        length.append(len(test))
        if test in sequences:
            pass
        else:
            sequences.append(test)
    else: continue
length = list(dict.fromkeys(length))
print("\nLongest possible sequences without shuffling the data but randomly picked at first: "+str(max(length))+"\nThe possible sequences are:")
for i in sequences:
    if len(i) == max(length):
        print(i)