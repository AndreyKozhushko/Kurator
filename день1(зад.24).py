import datetime
def printTimeStamp(name):
    print('Овчарнеко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

import math
s = int(input('Длина стороны:'))
n = int(input('Количество сторон:'))
r = s**2 * n
v = math.pi / int(n)
e = (math.tan(math.radians(v))) * 4
w = r / e
print(round(w,2))
