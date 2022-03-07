def convert_temp():
    tf = eval(input("Enter temperature in Fahrenheit: ",))
    tc = convert_to_celcius(tf)
    tk = convert_to_kelvin(tc)
    print("\nThe temperature in Fahrenheit is:",tf)
    print("The temperature in Celcius is:",tc)
    print("The temperature in Kelvin is:",tk)

def convert_to_celcius(f):
    tc = 5/9*(f-32)
    return tc

def convert_to_kelvin(c):
    tk = c+273.15
    return tk

convert_temp()



    
    