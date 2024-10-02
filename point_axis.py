x , y = [int(n) for n in input("x,y: ").split()]
if x==0 and y!=0:
    print("The point lies on y-axis ")
elif x!=0 and y==0:
    print("The point lies on x-axis ")
elif x==0 and y==0:
    print("The point lies on origin ")
else:
    print(x,y)
    
    