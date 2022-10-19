

from dataclasses import replace


#name = input('Name :')
#age = int(input('Age : '))
#address = input('Address : ')


#print('Your name is : ',name , '\nfand Age is : ' , age , '\nAddress is : ' , address)

sentence = input('Write a sentence :')
replace = input('What do you want to replace :')
requestreplace  = input('into : ')

newreplaced = sentence.replace(replace,requestreplace)




print('Your sentence is ' , sentence)
print('Requested replacement for ' , replace)
print('Your new sentence with replacement ',newreplaced)