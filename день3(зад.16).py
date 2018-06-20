import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))





def rec(x, y):
    if y == 0:
        return 1
    else:
        return x * rec(x, y - 1)


print(rec(2, 10))


