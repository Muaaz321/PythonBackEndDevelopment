class myClass:
    x = 5

p1 = myClass()
print(myClass.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name,' -- ', age , 'From the object')
        #pass # we can keep empty by saying pass , not trigger any error 


Name = input('Enter your name : ')
Age = input('Enter your age : ')

p1 = Person(Name,Age)

print(p1.age , 'from the instance')
print(p1.name, 'from the instance')

del p1 # we can delete the object
print(p1.name , p1.age)