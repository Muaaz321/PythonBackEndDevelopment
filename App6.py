from unicodedata import name


def welcome(name,age):
    print('Welcome : ' , name , ' Your age is : ' , age)


myname = input('What is you name : ')
myage = input('What is your age : ')
welcome(myname,myage)