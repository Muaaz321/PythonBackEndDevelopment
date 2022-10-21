# Functions
# intendation is important 

from os import name
import string


def greetings_functions(name,age):
    print('Welcome : ' , name , 'Your age is ', age) 
    #print('Welcome : ' + name) # this wont work when we pass integer with '+'
    #enforce parameter to String as below
    print('Welcome : ' + str(name) + 'Your age is :' + str(age)) 

greetings_functions('Haya',4)
greetings_functions(name='Muaaz',age=38)


def greetings_functions1(*names):
    print('Welcome : ' , names[1])
    print('Welcome : ' + names[2])
    print('Welcome : ' , names)

greetings_functions1('Muaaz','Haya','Fiwaza')


name = string('Enter your name : ')
age = string('Enter your age : ')
greetings_functions(name,age)