def calc_new_height():
    cur_width = eval(input("Enter the current width: "))
    cur_height = eval(input("Enter the current height: "))
    des_width = eval(input("Enter the desired width: "))
    corr_height = des_width/cur_width*cur_height
    print("\nThe corresponding height is:",corr_height)
    print(corr_height)
    return corr_height

calc_new_height()
        
    