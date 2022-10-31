print('Create Credentials')
username1 = input('Create your username : ')
password1 = input('Create your password : ')

print('Account created !!! ')

username2 = input('Login : ')
password2 = input('Password : ')

if username1==username2 and password1==password2:
    print('Successfully Loged In')
else:
    print('Unsuccessful login , try next time ')


def say_hi():
    print('Hi from App16')