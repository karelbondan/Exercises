users = {
    'dai':'yo',
    'xiez':'meh',
    'draz':'rawr'
}

def accept_login(users,username,password):
    list1 = []
    list1.append(username)
    list1.append(password)
    zipp = tuple(list1)
    for i in users.items():
        if zipp==i:
            return True
        else:
            continue
    return False


if accept_login(users, 'draz', 'rawr'):
    print("login successful!")
else :
    print("login failed!")