import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))



small = int(input("Количество бутилок меньше 1 л: "))
big = int(input("Количество бутилок больше равно 1 л: "))
money = small * 0.10 + big * 0.25
print("%.2f $" % money)

