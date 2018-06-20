import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




def rec(x):
    if x == 1:
        return 1
    else:
        return (1 / x) + rec(x - 1)

print(rec(5))


