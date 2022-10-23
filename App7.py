from unicodedata import name


my_dict ={
    'name':'Muaaz',
    'name' : 'Haya',# duplicate not allowed
    'name1' : 'Fiwaza',
    'nationality' : 'Sri Lankan',
    'qualification' : 'MBA',
    'age' : 38,
    'height' : 5.5,
    'friends' : ['Mick','Abdel','Rock','Peter']
}

print(my_dict)
print(my_dict['age'])
print(my_dict['height'])
print(my_dict['nationality'])
print(my_dict['friends'])
print(type(my_dict))

# Assign to a variable
namefrom = my_dict['name']
agefrom = my_dict['age']
print(namefrom)
print(agefrom)