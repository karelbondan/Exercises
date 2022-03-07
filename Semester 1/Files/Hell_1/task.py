file = None
with open("task.csv", 'r') as f:
    file = f.read()
data = file.split("\n")
dicti = {}
sort_val = []
mis_val = 0
test = None
for line in range(len(data)):
    test = data[line].replace('"', "").split(",")
    if test[0] == 'NA':
        mis_val += 1
    elif line > 0:
        if len(test) == 1: break
        dicti.setdefault(test[1], 0)
        dicti[test[1]] = dicti[test[1]] + int(test[0])
for items in sorted(dicti.values()):
    sort_val.append(items)
    if len(dicti.values()) % 2 == 1:
        test = len(dicti.values()) // 2
    elif len(dicti.values()) % 2 != 1:
        test = (len(dicti.values()) + len(dicti.values()) // 2)
print("Average steps: " + str(round(sum(dicti.values()) / len(dicti), 2)))
print("Median steps: " + str(sort_val[test]))
print("Missing values: " + str(mis_val) + " rows")