import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(float(input('Введите температуру:')))
b = int(float(input('Введите скорость ветра:')))
WCI = 13.12 + 0.6215 * a - 11.37 * b**0.16 + 0.3965 * a * b**0.16
if a <= 10 and b > 4.5:
  print(WCI)
elif a > 10 or b < 4.5:
  print('Что то ввели не так')
