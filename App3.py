# List 

countries = ['Sri lanka','India','Pakistan','Maldives','Nepal','Brunei','Bangladesh',True,False,23, 23.443,'Australia','Scotland',]
newcountries = list(('Dubai','Alaska','Denver',True,344.44,False,23))
print(newcountries)
print(type(newcountries))


print(countries)
print(countries[1][2]) # get first index and second index letter
print(countries[1:]) # print without zero index
print(countries[2:4]) # specifying a range
print(type(countries)) # identifying a type of a variable or list
print(type(countries[7]))
print(type(countries[8]))
print(type(countries[9]))
print(type(countries[10]))

# replace the list items
countries[0] = 'United Kingdom'
countries[2] = 'Saudi Arabia'


# print from back 
print(countries[-1])
print(countries[-2])
# length
print(len(countries)) 