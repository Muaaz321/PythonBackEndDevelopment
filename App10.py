number = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))

sign = input('Enter the sign : ')

def callthecalculation(number,number2,sign):
    if(sign=='+'):
        return print ('Addition : ', number+number2)
    elif(sign=='-'):
        return print('Minus : ', number-number2)
    elif(sign=='*'):
        return print('Multiply : ', number*number2)
    elif(sign=="/"):
        return print('Division : ', number%number2)
    else:
        return print('Unrecognized sign ')

callthecalculation(number,number2,sign)
