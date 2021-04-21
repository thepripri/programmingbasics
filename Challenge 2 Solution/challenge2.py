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

