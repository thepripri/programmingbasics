import os, math
from os import system 
from colorama import Fore, Back, Style 
from math import pow 

system('clear')

isNotZero = False 


# --- Functions ----

def printText(name):
    print(f'hello, {name}')


def calculate(num1, num2, marker):    
    if(marker == 'add'):
        operation = num1 + num2 
    elif(marker == 'subtract'):
        operation = num1 - num2 
    elif(marker == 'multiply'):
        operation = num1 * num2 
    elif(marker == 'divide'):
        if (num2 == 0):
            try:
                operation = num1 / num2 
            except ZeroDivisionError: print(f'Not possible division by {n2}')
        else:
            operation = num1 / num2 
    elif(marker == 'modulus'):
        operation = num1 % num2 
    elif(marker == 'power1'):
        operation = num1 ** num2 
    else:
        operation = pow(num1, num2) 
    return operation


# ----------- User input -----
n1 = int(input('Enter first number >> '))
n2 = int(input('Enter second number >> '))
fname = input("What is your first name? >> ")
# -------- end of User input ----

# ---- Calling functions -----
addition = calculate(n1, n2, 'add') 
subtraction = calculate(n1, n2, 'subtract')
multiplication = calculate(n1, n2, 'multiply')
division = calculate(n1, n2, 'divide')
modulus = calculate(n1, n2, 'modulus')
exponent1 = calculate(n1, n2, 'power1')
exponent2 = calculate(n1, n2, 'power2')

# ---- end of calling functions -----

# -- Print values ----
print(f'The sum of {n1} and {n2} is {addition}')
print(f'The subtraction of {n1} and {n2} is {subtraction}')
print(f'The multiplication of {n1} and {n2} is {multiplication}')
print(f'The division of {n1} and {n2} is {division}')
print(f'The modulus from division of {n1} and {n2} is {modulus}')
print(f'{n1} elevated to the power of {n2} is {exponent1} from function powerOf1')
print(f'{n1} elevated to the power of {n2} is {exponent2} from function powerOf2')


print()
print('---------------------')
printText(fname)
print('---------------------')
