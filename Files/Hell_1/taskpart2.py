import datetime
file = None
file2 = open('task2.csv', 'w')
with open("task.csv", 'r') as f:
    file = f.read()
data = file.split('\n')
test = None
ai = ""
counter = 0
for line in range(len(data)):
    test = data[line].replace('"', "").replace('NA', '0').split(",")
    if line > 0:
        if len(test) == 1: break
        if test[1][8] == '0':
            if datetime.datetime(int(test[1][:4]), int(test[1][5:7]), int(test[1][9])).weekday() < 5:
                test.append('weekday')
            else:
                test.append('weekend')
        elif test[1][8] != '0':
            if datetime.datetime(int(test[1][:4]), int(test[1][5:7]), int(test[1][8:])).weekday() < 5:
                test.append('weekday')
            else:
                test.append('weekend')
    else:
        test.append("daytype")
    for moo in test:
        counter += 1
        if counter <= 3: ai = ai + moo + ','
        else:
            ai = ai + moo + "\n"
            counter = 0
file2.write(ai)
file2.close()