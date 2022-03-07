def remove_keys(mydict, keylist):
    for i in list(mydict):
        if i in keylist:
            mydict.pop(i)
    return dict(mydict)

print(remove_keys({'1':'hi', '2':'hello', '3':'bleh'}, ['1','3','5']))
print(remove_keys({'5':'hi', '6':'hello', '1':'bleh'}, ['1','3','5']))
print(remove_keys({'4':'hi', '3':'hello', '7':'bleh'}, ['1','3','5']))