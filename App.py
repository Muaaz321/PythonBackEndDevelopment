from math import *

## String Functions ##

print('Hello World')
print('Welcome')

print('My Name is Muaaz , and age is ',38)


name = 'Muaaz'
age = 38

print(name+' is a boy')
print(name,' is ' , age)
print(name,' is from Colombo')

print(name)

# print next line
print('Hi\n how are you !!!')

# print slash in python
print('Hi. \How is Life')

# print character from the string
print(name[3])

namex = 'MUAAZ'
# convert to uppercase
print(name.upper())

# check whether it is lower
print(namex.islower())
# other functions try
print(namex.find('Z'))

# adding fucntions together
# convert a lower and then checking whether it is lower
print(namex.lower().islower())

# find the length 
print(len(namex))

# find out a charater in a string
print(namex.index('A'))

# replace character in the string
print(namex.replace('A','T'))

## Integer ##

number = 79;
print(78)
print(number)
print(78+22)
print(78+22.44)
print(78*4)
print(50-30)
print(20%6) # find out the reminder

number = 55;
number1 = str(number) # convert number to string
print('Is this a number'+number1)

print(-5) 
print(abs(-5)) # to avoid signs
print(max(4,5,4,30,22,3,11)) # retireve highest number
print(min(4,5,4,30,22,3,11)) # retrieve lowest number
print(round(3.5)) # making round
print(bin(332)) # retrieve binary functions

print(sqrt(100)) # retrieve sqaure , from math import