

try:
    x = int(input('Enter a Integer : '))
    print(x)
except:
    print('This is not a integer ')
else:
    print('nothing went wrong ') # will print only if successfull
finally:
    print('After try except') # will print after try and except


try:
    x = int(input('Enter a Integer : '))
except ValueError:
    print('This is not a integer ' + name)