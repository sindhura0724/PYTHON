##programs

#[1]

'''students = {
    'sindhu':22 , 'priya':21 , 'jacky' : 20
}

stud = students
students = {}
print(stud)
print(students)'''

#[2]

'''lst = ['sachin','dhoni','virat','rahul']
d = dict.fromkeys(lst,50)
print(d)
print(len(d))
print(len(lst))'''

#[3]
'''import operator
d = {
    'oil':230 , 'clip':150 , 'stud':175 , 'nut':35
}
print("original dictionary :",d)
d1 = sorted(d.items())
print("asc.order of d: ",d1)
d2 = sorted(d.items(),reverse=True)
print('dsc.order of d: ',d2)

d3 = sorted(d.items(),key = operator.itemgetter(1))
print('ASC ORDER of d by values: ',d3)
d4 = sorted(d.items(),key = operator.itemgetter(1),reverse=True)
print('DSC ORDER of d by values: ' ,d4)
'''

#[4]

'''d1 = {'mango':30 , 'guava':20}
d2 = {'apple':70 , 'pineapple':50}
d3 = {'kiwi':90 , 'banana':35}

d4 = {}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

d5 = {**d1,**d2,**d3}
print(d5)

d6 = (*d1,*d2,*d3)
print(d6)'''

#[5]
'''d1 = {'sindhu':1}
if not bool(d1):
    print('The dict is not empty')
if bool(d1):
    print('The dict id not empty')
d2 = {}
if not bool(d2):
    print("The dict is empty")
if bool(d2):
    print("The dict id empty")'''
    
    
#[6]
 
'''boys = {
     'nitesh':41,'nadeem':42,'ankit':43
}
girls = {
    'rashika':38,'shree':47,'priya':45
}
combined = {**boys,**girls}
print(combined)'''

#[7]

'''d = {
    'anuj':{'sal':10000,'age':20,},
    'aditya':{'sal':6000,'age':26},
    'rahul':{'sal':7000,'age':25}
}

lst = []
for i in d.values():
    lst.append(i['sal'])
print('max sal:',max(lst))
print('min sal:',min(lst))
 '''
 
#[8]
 
'''stud = {
    554:'ajay',350:'ramesh',395:'rakesh'
}    

roll_no = int(input('enter the roll_no: '))
name = stud.get(roll_no,'student')
print(f'congratulations {name}!')'''



##attempting the answers 

#[a]
'''# Predefined input string
input_string = input()

# Initialize an empty dictionary to store frequency of each character
frequency_dict = {}

# Count the frequency of each character in the string
for char in input_string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

# Print the frequency of each character
print("Character frequencies:")
for char, freq in frequency_dict.items():
    print(f"{char}: {freq}")

# Print the histogram
print("\nHistogram:")
for char, freq in frequency_dict.items():
    print(f"{char}: {'*' * freq}")'''

#[b]
 
'''stu = {
    'A' :{'math':98,'science':96,'social':99},
    'B' :{'math':99,'science':66,'social':89},
    'C' :{'math':90,'science':95,'social':88}   
}
 


for a,b in stu.items():
    tot_marks = sum(b.values())
    average = tot_marks/len(b.values())
    print(f'tot marks of students: {stu}:{tot_marks}')
    print(f'tot marks of students: {stu}:{average}')'''

#[c]

'''portfolio = {
    'accounts':['SBI','IOB'],
    'shares':['HDFC','ICICI','TM','TCS'],
    'ornaments':['10 gm gold','1 kg silver']
}

portfolio['MF']= ['reliance','ABSL']
print(portfolio)
portfolio.update({'accounts':['Axis','BOB']})
print(portfolio)
portfolio['shares'].sort()
print(portfolio)
del portfolio['ornaments']
print(portfolio)'''

#[d]

'''d1 = {
    'apple':{'price':60},
    'banana':{'price':30},
    'chocolate':{'price':20}
}

d2 = {
    'apple':6,
    'banana':12,
    'chocolate':1
}
tot_bill = ((d1['apple']['price'])*(d2['apple']))+((d1['banana']['price'])*(d2['banana']))+((d1['chocolate']['price'])*(d2['chocolate']))
print('total bill: ',tot_bill)
print(d1['apple'],d2['banana'])'''

#[f]
'''user_data = {}
for i in range(1,6):
    name = input()
    password = input()
    user_data[name]=password
print('usernames and passwords: ',user_data)

u_d1 = input()

if u_d1 in user_data:
    print('the match found')
else:
    print('the match not found')
    '''

#[g]

'''marks = {
    'subu':{'maths':88,'eng':60,'sst':95},
    'Anmol':{'maths':78,'eng':68,'sst':89},
    'raka':{'maths':56,'eng':66,'sst':77}
}

print(marks['Anmol']['eng'])

marks['raka']['maths']=77
print(marks)
print(sorted(marks.keys()))
print(marks)'''


#[h]

'''dict1 = {
    1:{'interface':'eth0' , 'ipadd':'1.1.1.1','status':'up'},
    2:{'interface':'eth1' , 'ipadd':'2.2.2.2','status':'up'},
    3:{'interface':'wlan0' , 'ipadd':'3.3.3.3','status':'down'},
    4:{'interface':'wlan1' , 'ipadd':'4.4.4.4','status':'up'},
}
print(dict1[3]['status'])

interfaces = []
for i,j in dict1.items():
    if j['status']=='up':
        interfaces.append((j['interface'],j['ipadd']))
print(interfaces)

print(len(dict1))

dict1[5]={'interface':'wlan2' , 'ipadd':'5.5.5.5','status':'down'}
dict1[6]={'interface':'wlan3' , 'ipadd':'6.6.6.6','status':'up'}
print(dict1)'''


#[i]

dict1 = {'a':1 , 'b':2, 'c':3 , 'd':4 , 'e':5}
print(dict1.popitem())
print(dict1.popitem())
print(dict1.popitem())
print(dict1.popitem())
print(dict1.popitem())
print(dict1)
    





    
