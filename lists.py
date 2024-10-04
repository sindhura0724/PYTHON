'''lst = []
if not lst:
    print("Empty list ")
   
print(bool(lst))'''
'''
lst = [10,2,0,50,4]
print(lst[::-1])'''


##programs::
'''lst = ['Anil','Anmol','Aditya','Avi','Alka']
print(lst)
lst.insert(2,'Anuj')
print(lst)
lst.append('Zulu')
print(lst)
lst.remove('Avi')
print(lst)
i = lst.index('Anil')
lst[i] = 'Anilkumar'
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)'''

'''lst = [1,3,5,7,9]
print(lst)

lst1 = [2,4,6,8,10]
print(lst1)

lst = lst + lst1
print(lst)

lst = [11,17,29]+lst
print(lst)

print(len(lst))

lst[-3:]=[100,200,300]
print(lst)

lst = []
print(lst)

del lst'''

#stack - LIFO
'''s = []
print (s)
s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())
print(s)'''

#Queue - FIFO


'''import collections
q = collections.deque()
q.append('sameera')
q.append('suhana')
q.append('shakira')
q.append('samaira')
q.append('sara')
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)'''

#RANDOM
'''import random
a = []
i = 1
while i<=20:
    num = random.randint(10,100)
    a.append(num)
    i+=1
print(a)

for num in a :
    if num>20 and num<50:
        a.remove(num)
print(a)'''

'''mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j]+mat2[i][j]
print(mat3)'''


##problems

#[a]

'''lst = [1,3,5,7,9]
lst1 = [2,4,6,8]
lst2 = [1,3,*lst1,7,9]
print(lst2)
lst2.sort()
print(lst2)
'''
#[b]
'''import random
a = []
i = 0
while i <=20:
    num = random.randint(10,100)
    a.append(num)
    i += 1
print(a)

for num in a:
    print(a.index(num)," ",num)'''
    
#[c]

'''a = [1,2,5,6,4,3,4,2,8,9,7,5,7,3,6,4,8,9,2,6]
b = []
for i in a:
    if i not in b:
        b.append(i)
b.sort()
print(b)'''

#[d]

'''a = [1,2,3,4,5,6,7,8,9,10]
e = []
o = []
i = 1 
for i in a :
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
print(e)
print(o)'''

#[e]

'''name = ['sindhu','samaira','sameera','sara','siri']
x = [s.upper() for s in name]
print(x)
'''
#[f]

'''f = [94,96,45,35,68,72]
i = 0
for i in f:
    c = (5/7)*(i-32)
    i +=1
    print(c)'''
    
#[g]

'''import statistics
a = [1,5,6,7,4,3,8,9,1]
median = statistics.median(a)
print("median: ",median)'''

#[h]
'''a = [-1,-5,-7,-6,-3,2,4,8,6,9]
i = 0
p = []
n = []
for i in a:
    if i>0:
        p.append(i)
    else:
        n.append(i)
print("positive integers:",p)
print("negative integers:",n)'''

#[i]
'''words = ['Apple','Banana','Cat','Dog','Egg']
letters = [word[0] for word in words]
print(letters)'''

#[j]
'''
a = [1,5,4,7,9,6,3,2,8,1,0]
b = []
i = 0
for i in a :
    if i not in b:
        b.append(i)
b.sort()  
print(b)'''


#[k]
import statistics
a = [1,2,3,4,5,6,7,8,9,10]
mean = [statistics.mean(a)]
median = [statistics.median(a)]
mode = [statistics.mode(a)]
print('mean: ',mean,'median: ',median,'mode: ',mode)



        



        

     
 


