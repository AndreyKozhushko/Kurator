import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

import math

number=int(input())

for i in range(2, int(math.sqrt(number)) + 1): 
    while (number % i == 0): 
        print(i)
        number //= i 

if (number != 1):
    print (number)
