import os 
from os import system

system('clear')

carTuple=('Toyota', 'Hundai', 'Nisan', 'Honda', 'Mercedes', 'BMW', 'Porsche', 'Tesla', 'kia', 'mazda')
carList = []
indexesToDelete = []

for data in carTuple:
    carList.append(data)

for car in carList:
    print(car)

#carList.clear()
#del carList[:]
#carList[:] = []

# Workaround to delete every SINGLE element in a list
counter = len(carList) - 1
for index in range(len(carList)):
    indexesToDelete.append(counter)
    counter-=1

for index in indexesToDelete:
    del carList[index]

print('------ Deleted -----')
for car in carList:
    print(car)

print(carList)

# BONUS Question 13:

namesList = ['Dunieski', 'Nathan', 'Priya', 'Yukta', 'Priyanka', 'Wendy', 'Yanet', 'Bryan', 'John', 'Kenneth']
agesList = [20, 21, 22, 23, 24, 22, 25, 27, 19, 20]

myNamesAndAgesDictionary = {}

for index in range(len(namesList)):
    myNamesAndAgesDictionary[namesList[index]] = agesList[index]

#names_dictionary[key] = value
myNamesAndAgesDictionary['Abdul'] = 25

for key, value in myNamesAndAgesDictionary.items():
    print(f"'{key}': {value}")



