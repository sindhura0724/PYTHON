'''
i = 1
while 1:
    print(i,end=' ')
    i+=1
    if i>10:
        break
'''
'''   
# all combination of 1 2 3
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i==j or j==k or k==i:
                k+=1
                continue
            else:
                print(i,j,k)
            k+=1
        j+=1
    i+=1
'''
#decimal value from binary value

b = int(input("Enter the binary value: "))
decimal = 0
power = 1

while b>0:
    last_digit = b % 10
    decimal = decimal +(last_digit*power)
    power = power*2
    b = b//10

print("decimal value of b: ",decimal)

                
    