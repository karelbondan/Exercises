def find_value(mydict, val):
    mydict_new = []
    for i in mydict.items():
        for j in val:
            if i[-1] == j:
                mydict_new.append(i)
    return list(dict(mydict_new))

print(find_value({'1':'hi', '2':'hello', 'ahowhaohow':'hi'}, ['hi']))
print(find_value({'1':'bro', 4:'bro', 3:'hi bro'}, ['bro']))