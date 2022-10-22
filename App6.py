from tokenize import Double
from unicodedata import name


def welcome(name,age):
    print('Welcome : ' , name , ' Your age is : ' , age)


# myname = input('What is you name : ')
# myage = input('What is your age : ')
# welcome(myname,myage)


def my_function(num1,num2):
    return num1 + num2
    print('Hello') # this wont print , because it is out side of the block


# number1 = int(input("Enter number one : "))
# number2 = int(input("Enter number two : "))
# print(my_function(number1,number2))


# myNumber = int(input('Enter a number : '))
# if(myNumber/2) :
#     print("This is a Even Nuumber")
# else: 
#     print("This is a Odd Number")


# def find_EvenNumber(no):
#     if(no%2==0) :
#         print("This is a Even Number ")
#     else:
#         print("This is a ODD Number ")

# num1 = int(input('What is you Number '))
# find_EvenNumber(num1)


# a = False
# b = 5
# if a== True:
#     print('A is true')
# elif a==False:
#     print('A is false')
# else:
#     print('A is none of those')

# boy = True
# short = True
# if boy == True or short == False: # if boy == True and short == False: 
#     print("He is a boy")
# elif boy == False:
#     print('A is false')
# else:
#     print('A is none of the two')


# value = input('input a value : ')
# if type(value)== str:
#     print(value , 'This is a String')
# else:
#     print(value , 'This is not a String')


sentence = input('Enter a sentence :')

if(len(sentence)<10):
    print('This is less than 10 words')
else:
    print('This is more than 10 words')

