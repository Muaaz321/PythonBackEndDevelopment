
myFile = open('Countries.txt','r') # a = append , r+ = read and write , w = only write , r = only read

print(myFile.readable())
print(myFile.readline())

print(myFile.readlines())

for lines in myFile.readlines():
    print(lines)

myFile.close

myNewFile = open('Country.txt','a')
myNewFile.writelines('\nThis is my new line from Python')

# creating a python file
myPythonfile = open('new.py','w')
myPythonfile.writelines('print(\'Hello i m from write file\')')