
from re import I


i = 1
while i < 10:
    print(i)
    i = i + 1 
   # i =+ 1


i = 1
while i < 10 or i== 10:
    print(i)
    i = i + 1
   # i =+ 1

for x in 'Hello':
    print(x)


mylist = ['qa','dev','ba','devops']
for item in mylist:
    print(item)
    if item=='dev':
        break

myDic = {
    'id': 34,
    'name' : 'max',
    'address' : 'colombo',
    'price' : 56.77
}
for myitems in myDic:
    print(myitems)
    if myitems == 'address':
        break
else:
    print('Finish looping')


for x in range(5):
    print(x)
else:
    print('Finish looping')


for y in range(5,10):
    print('****')
    print(y)