import calendar

month = int(input("Enter your preferred month in integer: ",))
year = int(input("Enter your preferred year in integer: ", ))
print(calendar.month(year, month, w=0, l=0))