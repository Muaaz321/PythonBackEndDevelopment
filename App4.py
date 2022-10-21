# Tuples is immutable , can not change variable
# can store multiple values in single variable

three_number = (1,2,3,1)
#three_number[1] = 22 # this wont allow
print(three_number[0])
print(three_number)
print(type(three_number))

string = ('qa','dev','po','devops')
boo = (True,False)
print(string,boo)

mixedtogether = (1,3,'Name','Address',True,False,34.33)
print(type(mixedtogether[0]))
print(type(mixedtogether[2]))
print(type(mixedtogether[4]))

content = tuple((1,3,'String',True,'Name',False,30.33)) # another way of defining tuple
print(content)