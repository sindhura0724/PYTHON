'''num = int(input("Enter the num: " ))
while num != 5:
    print(num,num*num)
    num = int(input("Enter the num: " ))
    '''
'''count = 0
while count <=10:
    print(count,count*count,count*count*count)
    count +=1'''
'''   
s = "mumbai"
lst = ['desert','dessert','to','too','lose','loose']
#tpl = (10,20,30)
i = 0
while i<len(lst):
    print(i,s[i],lst[i])#,tpl[i])
    i +=1
'''
'''
lst =  ['desert','dessert','to','too','lose','loose']
for i,ele in enumerate(lst):
    print(i,ele)'''

'''
    
for index in range(20,10,-3):
    print(index,end=' ')'''

'''
j = 1 
while j<=10:
    print(j)
    j+=1
'''
'''
while True:
    print("Infinite loop")
'''     
'''
lst = [10,20,30,40,50]
for i in range(5) :
    print(lst[i])
'''
'''
i = 15
while i>=10:
    print(i)
    i-=1
'''
'''
for alpha in range(65,91):
    print(chr(alpha),end=' ')'''
'''   
for i in range(0.1,1.0,0.25):
    print(i)
    #solution for the above 
i = 0.1
while i<1.0:
    print(round(i,2))
    i+=0.25'''
'''    
i = 1
while i <=10:
    j = 1
    while j<=5:
        print(i,j)
        j += 1
        break
    print(i,j)
    i+=1'''
    
    
# RCI chap-6 last programing solutions

#(A)
'''
for i in range (1,25,2):
    print(i,end = ' ')
    
    '''
#(B)
'''
s = "mumbai"
lst = ['desert','dessert','to','too','lose','loose']
i = 0
for i , ele in enumerate(lst): 
    if i>3:
        break
    else:
        print(i,lst[i],s[i])
        i+=1
'''
#(C)
'''
s = 'Nagpur-440010'
a = 0
d = 0
for i in s:
    if i.isalpha():
        a+=1
    elif i.isdigit():
        d+=1

print(a)
print(d)

'''
#(D)
'''
num =  input("Enter the number : ")

num1 = num[::-1]
print(num1)
if num == num1:
    print('equal')
else:
    print('not equal')
'''
#(E)
'''
n = int(input("enter the number: "))
fact = n
i = 1
while i<n:
    fact = fact*i
    i+=1
print(fact)
'''

#(F)


'''for n in range(1,500):
    sum = 0
    temp = n
    

    while temp>0:
        num = temp%10
        sum += num**3
        temp = temp//10
        
    if n == sum:
        print(n,end = ' ')'''
    
'''
    
for n in range(1,501):
    digits = [int(digit) for digit in str(n)]
sum=0
for digit in digits:
    sum += pow(digit,3)
if n==sum:
    print(n)
'''

#(G)
'''for num in range(1,300):
    is_prime = True

    for i in range(2,int(num**0.5)+1):
        if num % i == 0: 
            is_prime = False
            break 
    
    if is_prime:
        print(num,end = ' ')'''
        
#(h)

n = int(input("Enter the table number: "))

for i in range(1,11):
    result = n*i
    print(n," * ",i ,"= ",result)
    