import os 
from os import system
from colorama import Fore, Style

system('clear')

tuple1 = (23, 45, 12, 56, 78, 34, 12, 78, 89) # -> 427
tuple2 = (27, 39, 18, 50, 75, 33, 17, 70, 90) # -> 419  -> 846
numTotal = 0
evenTotal = 0
oddTotal = 0

# 1. Add all the numbers in them using a for loop
for index in range(len(tuple1)):
    numTotal += (tuple1[index] + tuple2[index])
print(f'Total of Numbers: {numTotal}')

# 2. Find the total of all the even numbers in the tuples (all combined)
for index in range(len(tuple1)):
    if (tuple1[index] % 2 == 0): # -> 0 is remainder for even numbers
        evenTotal += tuple1[index]
    if (tuple2[index] % 2 == 0):
        evenTotal += tuple2[index]
print(f'Total Even: {evenTotal}')

# 3. Find the total of all the odd numbers in the tuple (all combined)
for index in range(len(tuple1)):
    if (tuple1[index] % 2 == 1): # -> 1 is remainder for odd numbers
        oddTotal += tuple1[index]
    if (tuple2[index] % 2 == 1):
        oddTotal += tuple2[index]
print(f'Total Odd: {oddTotal}')

# 4. In a for loop, accomplish the following
# Initialize an empty list
# The list is a list of dictionaries -> [Each dictionary is a person]
# Have the user enter how many dictionaries he or she wants to add to the list
# Each dictionary must contain the following
   # first name
   # last name
   # age
   # phone
   # address 1
   # address 2
   # city
   # state
   # zip code
# Print the list of dictionaries
# personList = []

# numOfPeople = int(input('Enter the number of people that you want to add >> '))

# for counter in range(numOfPeople):
#     personDictionary = {}
#     print('--------------------')
#     print(f' Person # {counter + 1}')
#     firstName = input('Enter your first name >> ')
#     personDictionary['firstName'] = firstName
#     lastName = input('Enter your last name >> ')
#     personDictionary['lastName'] = lastName
#     age = int(input('Enter your age >> '))
#     personDictionary['age'] = age
#     phone = input('Enter your phone >> ')
#     personDictionary['phone'] = phone
#     address1 = input('Enter address 1 >> ')
#     personDictionary['address1'] = address1
#     address2 = input('Enter address 2 >> ')
#     personDictionary['address2'] = address2
#     city = input('Enter your city >> ')
#     personDictionary['city'] = city
#     state = input('Enter your state >> ')
#     personDictionary['state'] = state
#     zipCode = input('Enter your zip code >> ')
#     personDictionary['zip'] = zipCode

#     # add the dictionary to the list
#     personList.append(personDictionary)

# print()
# counter = 1

# # nested for loop
# for dictionary in personList:
#     print(f'---- Dictionary # {counter} ----')
#     for key, value in dictionary.items():
#         print(f'{key}: {value}')
#     counter += 1

# 6. BONUS:
    # - Create a program that prompts users to select reservation packages [Bronze, Silver, and Gold] with their respective prices
    # - If Bronze is chosen, there is a bonus of $200
    # - If Silver is chosen, there is a bonus of $400
    # - If Gold is chosen, there is a bonus of $600
    # - Calculate subtotal, taxes, and grand total
    # - Display order details [colorama preferred]
    # - Use for loops seen in class, functions, and lists

system('clear')
packagesList = ['Bronze', 'Silver', 'Gold']
packagesPricesList = [15999.99, 18999.99, 20999.99]
counter = 1
BONUS = 0
packageTotalPrice = 0

def calculatePackagePrice(packagePrice, bonus, package):
    print()
    print(Fore.YELLOW, f'You have selected the {package} package')
    print()
    total = 0
    taxes = packagePrice * 0.07
    subTotal = packagePrice 
    total = subTotal + taxes - bonus 
    print(Fore.RED, '               ---- ORDER SUMMARY ----')
    print(Fore.MAGENTA, f'''
         Package:...................   {package} 
         Cost:...................... $ {packagePrice}
         Subtotal:.................. $ {subTotal}
         Taxes:..................... $ {round(taxes, 2)}    
         Bonus:..................... - $ {bonus}        
         GrandTotal:................ $ {round(total, 2)}
''')


print('---- AVAILABLE PACKAGES ----')
for index in range(len(packagesList)):
    print(f'{counter}. {packagesList[index]} -> ${packagesPricesList[index]}')
    counter += 1

while True:
    while True:
        selection = int(input('Enter an option above [1-3] >> '))
        if (selection == 1):
            BONUS = 200
            calculatePackagePrice(packagesPricesList[0], BONUS, 'Bronze')
            break
        elif (selection == 2):
            BONUS = 400
            calculatePackagePrice(packagesPricesList[1], BONUS, 'Silver')
            break
        elif (selection == 3):
            BONUS = 600
            calculatePackagePrice(packagesPricesList[2], BONUS, 'Gold')
            break
        else:
            print('invalid option')
    print(Style.RESET_ALL)
    choice = input('Do you want to purchase another package? [ Y/N ] >> ')  
    if (choice.upper() == "N"): 
        print('Thanks for using our services')
        break







    