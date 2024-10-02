for i in range(1,11):
    p = int(input("Enter the principal: "))
    q = int(input("Enter the interest compund: "))
    r = float(input("Enter the annual rate: "))
    n = int(input("enter the no.of years: "))
    a = round(p*(1+(r/q))**(n*q),2)
    print("The amount : ",a)
    i += 1