import datetime
def printTimeStamp(name):
    print('Овчаренко ИВан Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


name = input("Как вас зовут?")
print("Хаю хай " + name)


