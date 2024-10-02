x , y = [int(n) for n in input('x , y : ').split()]
h , k = [int(n) for n in input('h , k : ').split()]
r = float(input('radius: '))
p = float( pow(x-h,2)+pow(y-k,2) )
radius = pow(r,2)

if p<radius:
    print("The point lies within the circle")
elif p==radius:
    print("The point lies on the circle")
elif p>radius:
    print("The point lies outside the circle")
else:
    pass
