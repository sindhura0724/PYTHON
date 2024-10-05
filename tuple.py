#problems

'''result = divmod(16,4)        #divmod(quotient,remainder)
print(result)
t = (16,4)
res = divmod(*t)
print(res)'''

'''t = (10,20,30,40,50,60,70,80,90,100)
a,b,c,d,e,f,g,h,i,j = t
print(t)
print(a,b,c,d,e,f,g,h,i,j)

x,_,_,_,_,_,_,_,_,y = t
print(x,y,_)
i,*_,j = t
print(i,j,_)'''

'''t = ('sindhu','sam','sameera',('suresh',),('rajesh',),('rajiv',))
girl = 0
boys = 0
for ele in t:
    if isinstance(ele,tuple):
        boys +=1
    else:
        girl +=1
print("girls: ",girl,' ','boys: ',boys)'''


'''t = [
    (1,'sindhu',22),(2,'rashu',21),
    (3,'varshu',20),(4,'lucky',23),(5,'swati',23)
]

t1 = []
for i in t:
    t1 = t1+[i[1]]

print(t1)'''
 

'''t = ('F','l','a','b','b','e','r','g','a','s','t','e','d')
t = t + ('!',)
print(t)
s = ''.join(t)
print(s)
t1 = t[3:5]
print(t1)
c = t.count('e')
print(c)
print('r' in t)
l = list(t)
print(l)
t = t[:3]+t[7:]
print(t)'''

#exercises

#[b]

'''num1 = num2 = (10,20,30,40,50)
print(id(num1),type(num1))
print(isinstance(num1,tuple))
print(num1 is num2)
print(num1 is not num2)
print(20 in num1)
print(30 not in num1)'''

#[c]

'''from datetime import date

date1 = (20,2,2024)
date2 = (26,6,2024)

d1 = date(date1[2],date1[1],date1[0])
d2 = date(date2[2],date2[1],date2[0])

num_of_days = d2-d1
print(num_of_days)
'''

#[d]
'''import operator
lst = [
    ('blue',54.0),('pink',55.50),('black',86.36),('violet',26.63)
]
print(sorted(lst))                                  #sorted by name
print(sorted(lst,key = operator.itemgetter(1)))     #sorted by number'''


#[e]

'''share = (
    ('pink','24-6-20',56000,506,36000),('black','28-7-26',82000,604,92000)
    ,('red','7-6-20',1000000,606,100000900),('green','24-01-26',50000600,508,9540000)
)
portfolio = (sum(t[2] for t in share ) )
print(portfolio)

for i in share:
    if i[4]>i[2]:
        profit = (i[4]-i[2])*i[3]
        profit_per = (profit/i[2])*100
    elif i[2]>i[4]:
        loss = (i[2]-i[4])*i[3]
        loss_per = (loss/i[2])*100
    else:
        ('no profit no loss')

print(profit)
print(loss)
print(profit_per)
print(loss_per)'''


#[f]
 
'''lst = [('hi',),()]
t = [t for t in lst if t]
print(t)'''
 
#[g]

tpl = [
    ("a",1,100),('b',2,98),('c',3,97)
]
t1=t2=t3=[]
for i in tpl:
    t1 = t1+[i[0]]
    t2 = t2+[i[1]]
    t3 = t3+[i[2]]
    
print("tuple of names: ",t1)
print("tuple of roll_num: ",t2)
print("tuple of marks: ",t3)
     
