import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей : ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a, b, c = list(map(int, input("Enter 3 numbers").split()))
l = ["" for i in range(a+b+c)]
l[a] = a
l[b] = b
l[c] = c
print(" ".join(str(i) for i in l[::+1]))

