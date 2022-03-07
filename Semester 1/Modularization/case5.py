def overlapping(lst1, lst2):
    state = False
    while True:
        for i in lst1:
            for j in lst2:
                if i == j:
                    state = True
                    print(state)
                    break
                else:
                    continue
        count = len(lst2)
        if count == len(lst2):
            if state == True:
                break
            else:
                print (state)
                break

overlapping(['hello',4,7,8], ['hello', 2, 5, 6])
overlapping([1,2,3], [4,5,6])
overlapping(['hi yes it fockin works', 2,3], ['IT FOCKIN WORKS', 'hi yes it fockin works'])