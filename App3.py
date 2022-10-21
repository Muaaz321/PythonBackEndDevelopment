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


list1 = [1,2,3,4,5,6,7,8,9]
list2 = ['Green','White','Orange','Yellow','Red','Yellow']

list1.extend(list2) # merge two list together
print(list1)

list2.append('Purple') # add to the list
print(list2)

list2.insert(0,'Black') # insert a value inbetween a list
print(list2) 

list2.remove('Orange') # remove a item from the list
print(list2) 

list1.clear # to clear the list completely
print(list1)

print(list2.index('Yellow')) # to retrieve the index for particular item in the list

print(list2.count('Yellow')) # to retrieve number of string in that list

list3 = [50,32,11,2.11,4.56,0.32,400.9,503,2323224,34323.54,232,33]
list3.sort() # Ascending order
print(list3)

list2.reverse() # to reverse
print(list2)

list4 = list3.copy() # copy one list to another
print(list4)

list4.pop() # to remove last item in the list
print(list4)
list4.pop(1) # remove from index
del list4[2] # remove from the list - another way

#del list4 # delete entire list with all the items
