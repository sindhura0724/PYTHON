#programs

#[1]
'''lst = [num for num in range(2,51) if num%2 == 0 and num%4 == 0]
print(lst)'''

#[2]
'''mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
lst = [num for lst in mat for num in lst]
print(lst)'''

#[3]
'''import random
r = {random.randint(15,46) for n in range(10)}
print(r)
print(len(r))
r1 = len({n for n in r if n<30})
print(r1)
r2 = {n for n in r if n<30}
print(r2)
r3 = r-r2
print(r3)'''
 
#[4]
'''lst = [(),(),(10,20),('',),(10,20,30),(40,50),(),(45)]
lst = [tpl for tpl in lst if tpl]
print(lst)'''

#[5]
'''s1 = 'Dreams may change, but friends are forever'
s2 = [' '.join(w.capitalize()for w in s1.split())]
s3 = s2[0]
print(s3)'''

#[6]
'''words = {'Tub':1 ,'Toothbursh':2,'Towel':3,'Nailcutter':4}
d = {''.join(alpha for alpha in k if alpha not in'aeiou'):v for (k,v)in words.items()}
print(d)'''

#[7]
'''mat1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j]+mat2[i][j]
print(mat3) 
mat3 = [[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
print(mat3)'''

#[8]
'''a =[]
for n in range(10,30):
    if n%2==0:
        a.append(n)
print(a)

a = [n for n in range(10,30) if n%2==0]
print(a)'''
    
#[9]
'''# Input set
sent = {'Pack my box with five dozens liquor jugs'}

# Convert the sentence to lowercase and split into words
words = set(sent.pop().lower().split())

# Filter out words with a minimum length (for example, greater than 3 characters)
filtered_words = {word for word in words if len(word) > 3}

# Print the result
print(filtered_words)'''

#[10]
lst = [2,7,8,6,5,5,4,4,8]
s = {True if n%2==0 else False for n in lst}
print(s)




#problems...

#[a]
'''coordinates = [(x,y) for x in range(0,6) for y in range(0,6)]
print(coordinates)'''

#[b]
'''lst = [5,8,6,21,16]
new_lst = [x*10 for x in lst ]
print(new_lst)'''

#[c]
'''F = [0, 1]  # Initialize the first two Fibonacci numbers
[F.append(F[-1] + F[-2]) for _ in range(18)]  # Generate the next 18 Fibonacci numbers
print(F)  # F will now contain the first 20 Fibonacci numbers
'''
#[d]
'''x = [x for x in range(0,21) if x%2 != 0]
y = [y for y in range(0,21) if y%2 == 0]
print('odd nums: ',x,' ','even nums: ',y)'''

#[e]
'''lst = [1,2,3,4,5,6,7,8]
x_lst = [x for x in lst if x%2==0]
y_lst = [y for y in lst if y%2!=0]
print(x_lst,y_lst)'''

#[f]
'''st = ['hi','hello','hii','bye','good']
st1 = [x.title() for x in st]
print(st1)
 '''

#[g]
'''f_temp = [32,68,100,50,212]
c_temp = [(5/9)*(f-32) for f in f_temp]
print(c_temp)'''


#[h]
'''import numpy as np
A = np.random.randint(40,160,size=(4,5))
print(A)
'''

#[i]
'''lst = ['hello','i','am','sindhura','here']

s1 = [x.title() for x in lst ]
sets = set(s1)
print(sets)'''




