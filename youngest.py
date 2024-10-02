ram = int(input("age of ram: "))
shyam = int(input("age of shyam: "))
ajay = int(input("age of ajay: "))
if ram<ajay and ram<shyam:
    print("the youngest is ram ")
elif shyam<ram and shyam<ajay:
    print("the youngest is shyam")
else:
    print("the youngest is ajay")
    