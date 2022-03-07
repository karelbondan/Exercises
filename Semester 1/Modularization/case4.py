def is_member(val, a_list):
    state = False
    if val==a_list[0] or val==a_list[1] or val==a_list[2] or val==a_list[3]:
        state = True
        print(state)
    else:
        print(state)


is_member(1, [1, 2, 'hello', 30])
is_member('hi', [4,5,6,7])
is_member(5, [1,3,5,7])

#The downside of this code is we only can input 4 index inside the list, if less or more then it'll produce an error