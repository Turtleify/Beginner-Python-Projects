number1 = input('Enter your first number >> ')
num1 = int(number1)
sign = input('What operation would you like to do? ( + , - , * , / ) >> ')
number2 = input('Enter your second number >> ')
num2 = int(number2)

def calc():
    if sign == '+':
        print('The sum of your numbers is' + str(num1 +num2))
    elif sign == '-':
        print('The difference of your numbers is ' + str(num1 -num2))
    elif sign == '*':
        print('The product of your numbers is ' + str(num1 *num2))
    elif sign == "/":
        print('The quotient of your numbers is ' + str(num1 /num2))
    else:
        print('please use a valid input')

calc()