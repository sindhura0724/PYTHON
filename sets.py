##problems

'''a = {10,20,30,40,50,60,70}       
b = {33,44,51,10,20,50,30,33}
print(a|b)
print(a&b)                          
print(a-b)
print(b-a)
print(a^b)
print(a>=b)
print(a<=b)'''

#output
'''{33, 70, 40, 10, 44, 50, 51, 20, 60, 30}
{50, 10, 20, 30}
{40, 60, 70}
{33, 51, 44}
{33, 70, 40, 44, 51, 60}
False
False'''


#exercises

'''s = {1,2,3,7,6,4}
s.discard(10)
s.remove(10)
print(s)

output
 s.remove(10)
KeyError: 10
'''


'''s1 = {10,20,30,40,50}
s2 = {10,20,30,40,50}
print(id(s1),id(s2))


2486563132736 2486563132288'''


'''s1 = {10,20,30,40,50}
s2 = {10,20,30,40,50}
s3 = {*s1,*s2}
print(s3)

output
{40, 10, 50, 20, 30}
'''

'''s = set('KanLabs')
t = s[::-1]
print(t)

output
t = s[::-1]
        ~^^^^^^
TypeError: 'set' object is not subscriptable
'''

'''s = {10,20,30,{40,50},60}
print(s)

output
s = {10,20,30,{40,50},60}
        ^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'set'

'''

'''s = {'tiger','lion','jackal'}
del(s)
print(s)

output
 print(s)
          ^
NameError: name 's' is not defined'''

'''fruits = {'kiwi','mango','apple'}
fruits.clear()
print(fruits)

output
set()'''

'''s = {10,25,4,8,10,25}
sorted(s)
print(s)

output:
    {8, 25, 10, 4}'''
    
'''s = {}
t = {1,4,5,2,3}
print(type(s),type(t))

output:
    <class 'dict'> <class 'set'>'''


#programs
#[a]    
    
'''s = {'Ashish','Akash','Anirudh','Bunny','Brade','Brownie'}
A = set()
B = set()
for i in s:
    if i.startswith('A'):
        A.add(i)
    elif i.startswith('B'):
        B.add(i)
    else:
        pass
print(A)
print(B)'''
#[b,c]
'''s = set()
s.add('sindhu')
s.add('varshu')
s.add('jay')
s.add('rashu')
s.add('jake')
print(s)
t = {'lucky'}
print(t)
s.update(t)
print(s)
s.remove('jake')
s.remove('jay')
print(s)
s.discard('sindhu')
print(s)'''

#[d]
import random
s = set()

for i in range(0,11):
    t = random.randint(15,45)
    s.add(t)
    i+=1
    if t<30:
        c = len(s)
    elif t>35:
        s.remove(t)
    else:
        pass
        

print(s)
print(c)



    


