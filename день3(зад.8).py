import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

def mag(year, month, day):
    year = str(year)
    year2 = year[-2] + year[-1]
    if month * day == int(year2):
        print("Yes")
    else:
        print("No")

mag(1960, 10, 6)


