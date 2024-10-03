#examlpes::

'''name = ' sushant ajay raj '
for n in name.split():
    print(f'{n:10}')'''
    
'''radius = 1.5679
print('radius = {0:10.2f}'.format(radius))'''

'''name = "jay"
age = 22
print('name = {0:15} age = {0:10}'.format(name,age))'''

##problems::

#7.1

'''values = input("Enter the values of length, breadth and radius: ").split()
length = int(values[0])
breadth = int(values[1])
radius = float(values[2])
circumference = 2 * 3.14 * radius
perimeter = 2 * (length + breadth)
print('circumference = {} perimeter = {}'.format(circumference,perimeter))
'''

#7.2
'''x,y,z = [int(n) for n in input("Enter the values of x,y,z: ").split()]
for i in range(x,y,z):
    print(f'i = {i:>5} square = {i**2:>7} cube = {i**3:>9}')#right alligned
for i in range(x,y,z):
    print(f'i = {i:<5} square = {i**2:<7} cube = {i**3:<9}')#left alligned'''
    
#7.3

'''data = {
    'sindhura': 9182389201 , 'sindhu' : 6300262974 , 'jayanth' : 9390804329 , 'chowdary ': 7670889810
}
for name,cellno in data.items():
    print(f'{name:15}:{cellno:10}')
    '''
    
#7.4
'''min,max,mean,sd,var = input("Enter the values of min,max,mean,sd,var : ").split()
min , max , mean = int(min),int(max),int(mean)
sd , var = float(sd),float(var)

print(f'\n{'min :':<15}{min :>10}',
    f'\n{'max :':<15}{max :>10}',
    f'\n{'mean :':<15}{mean :>10}',
    f'\n{'sd :':<15}{sd :>10}',
    f'\n{'var:':<15}{var:>10}'
    )
    '''

#7.5
'''import math 
width = 10
precision = 4
for i in range (1,11):
    s = math.sqrt(i)
    c = math.pow(i,1/3)
    print(f'{i:5}{s:{width}.{precision}}{c:{width}.{precision}}')'''
    

#arbitary float nums
'''num = float, input().split()
print(num)
'''
#correct the code

'''x = 14.99
y = 114.39
print(
    f'\n{"x = ":4}{x:>10}\n{"y = ":4}{y:>10}'
) '''   

'''boolean = input("Enter the boolean value: ")
print(boolean)'''

'''price = 1.5567894
print(f'{price:10.4f}')'''

#avg of floats

'''nums = [float(n) for n in input("Enter the number: ").split()]
avg = sum(nums)/len(nums)
print("Average of nums: ",avg)'''

'''data = input("Enter the name,years_worked,bonus: ").split()
name = data[0]
years_worked = int(data[1])
bonus = float(data[2])
deduction = 2 * years_worked + bonus * 5.5 / 100
print("Agreement deduction: ",deduction)'''

'''print("Result = ",4>3)'''

a = 12.34
b = 234.39
c = 444.34
d = 1.23
e = 34.67
print(
    f'\n{"a = ":<5}{a:>10}',
    f'\n{"b = ":<5}{b:>10}',
    f'\n{"c = ":<5}{c:>10}',
    f'\n{"d = ":<5}{d:>10}',
    f'\n{"e = ":<5}{e:>10}',
)