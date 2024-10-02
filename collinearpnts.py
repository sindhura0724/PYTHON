x1,y1 = [int(n) for n in input("x1,y1: ").split()]


x2,y2 =[int(n) for n in input("x2,y2: ").split()]

x3,y3 = [int(n) for n in input("x3,y3: ").split()]

a = (x1 *(y2-y3))+ (x2 * (y3-y1))+ (x3 *(y1-y2)) 

if a == 0: print('yes')
else: print("no")




