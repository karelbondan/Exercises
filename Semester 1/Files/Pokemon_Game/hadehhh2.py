import hadehhh as h

count = 0
igaveupmysecondlastbraincellsforthis = []
while count <= 100000:
    count += 1
    test = h.game()
    if test != None:
        igaveupmysecondlastbraincellsforthis.append(len(test))
    else: continue
igaveupmysecondlastbraincellsforthis = list(dict.fromkeys(igaveupmysecondlastbraincellsforthis))
print(max(igaveupmysecondlastbraincellsforthis))