import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

import math
t1 = int(input('широта t1:'))
g1 = int(input('долгота g1:'))
t2 = int(input('широта t2:'))
g2 = int(input('долгота g2:'))
T1 = math.radians(t1)
G1 = math.radians(g1)
T2 = math.radians(t2)
G2 = math.radians(g1)
form = 6371.01 * math.acos(math.sin(T1)) * math.sin(T2) + math.cos(T2 ) * math.cos(T2 ) * math.cos(G1 - G2)
print(form)
