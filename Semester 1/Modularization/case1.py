def user_input():
    usrinput = list(map(str, input("Sample numbers: ",).split(",")))
    print("List: ", usrinput)
    print("Tuple: ", conversion1(usrinput))

def conversion1(x):
    for i in x:
        tuple1 = tuple(x)
    return tuple1

user_input()