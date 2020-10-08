def convert_to_days():
    hours = eval(input("Enter number of hours: "))
    minutes = eval(input("Enter humber of minutes: "))
    seconds = eval(input("Enter numbers of seconds "))
    print("\nThe number of days is:",get_days(hours, minutes, seconds))

def get_days(hours, minutes, seconds):
    z = hours, minutes, seconds
    days_calc = float((z[0]+z[1]/60+z[2]/3600)/24)
    days_4_dec = round(float(days_calc), 4)
    return days_4_dec

convert_to_days()
