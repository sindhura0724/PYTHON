'''msg = "Hello"
print(msg)
a=msg[0]
b=msg[4]
c=msg[-0]
d=msg[-1]
e=msg[-2]
f=msg[-5]
print(a,b,c,d,e,f)
print(msg[3:100])
print(msg[0:5])
print(msg[0:])
print(msg[:5])
print(msg[-1:])
print(msg[:-3])

print('-',10)

msg1='good'
msg2='morning'
msg3= msg1 + ','+msg2
print(msg3)

print('o' in msg1)
print(len(msg1))
print(min(msg1))
print(max(msg1))
print(type(msg1))
print(id(msg1))'''

'''
import random
num = random.randint(1,25)
s='hello'
print(s.upper())
print(num)
print(s.find('l'))
print(s.partition('e'))
print('-'.join(s))'''

#strings exercises

#strings with special characters
'''
msg1 = 'He said,\'let us python\'.'
file1 = 'C:\\temp\\newfile'
file2 = r'C:\temp\newfile'
print(msg1)
print(file1)
print(file2)'''

#multiline strings
#whitespaces at beggining of second line becomes part of string
'''
msg = 'What is this life if full of care...\
    We have no time to stand and stare'
print(msg)

#enter at the end of first line becomes part of string
msg1 = """What is this life if full care...
We have no time to stand and stare"""
print(msg1)

#strings are concatenated properly.()necessary
msg2 = ('What is this life if full of care...'
        'We have no time to stand and stare')
print(msg2)'''

#string replication during printing
'''
msg = 'McLearn!!'
print(msg*2)'''

#imuutability of strings
#utopia wont change but msg will
'''
msg = 'utopia'
msg1 = 'today!!'
msg = msg+' '+msg1
print(msg)


'''

#built-in function in strings
'''
print(len('Hoopla'))
print(min('Hoopla'))
print(max('Hoopla'))'''
'''
s = 'Bamboozled'
print(s[-2],s[-1])
print(s[::-1])'''
'''
s1 = 'NitiAayog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())'''


