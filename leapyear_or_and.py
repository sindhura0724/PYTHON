year = int(input("Enter the year: "))
lp = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if lp==True:
    print("It's a leap year")
else:
    print("It's not a leap year")
    