import os 
from os import system 
from colorama import Fore, Back, Style 

system('clear')

isNotZero = False 

# --- Functions ----
#        2     3
def add(num1, num2):
    addCalculate = num1 + num2 
 #  addCalculate = 2    +   3 
    return addCalculate
#   return 5

def subtract(num1, num2):
    subtractCalculate = num1 - num2
    return subtractCalculate

def multiply(num1, num2):
    multiplyCalculate = num1 * num2 
    return multiplyCalculate

def divide(num1, num2):
    if (num2 == 0):
        try:
           divideCalculate = num1 / num2
        except ZeroDivisionError: print(f'Not possible division by {n2}')
    else:
        divideCalculate = num1 / num2
        return divideCalculate
# -------------------

# ----------- User input -----
n1 = int(input('Enter first number >> '))
n2 = int(input('Enter second number >> '))
# -------- end of User input ----

# ---- Calling functions -----
#          add(2, 3)
addition = add(n1, n2) # n1 and n2 are arguments
#          --  5  ---
subtraction = subtract(n1, n2)
multiplication = multiply(n1, n2)
division = divide(n1, n2)

# ---- end of calling functions -----

print(f'The sum of {n1} and {n2} is {addition}')
print(f'The subtraction of {n1} and {n2} is {subtraction}')
print(f'The multiplication of {n1} and {n2} is {multiplication}')
print(f'The division of {n1} and {n2} is {division}')


