import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = int(input('Введите децибелы:'))
if a == 130:
  print('Jackhammer')
if a == 106:
  print('Gas Lawnmover')
if a == 70:
  print('Alarm clock')
if a == 40:
  print('Quiet room')
if a < 130 and a >106:
  print('Між Jackhammer та Gas Lawnmover ')
if a < 106 and a > 70:
  print('Між Gas Lawnmover та Alarm clock')
if a < 70 and a > 40:
  print('Між  Alarm clock та Quiet room')
elif a > 130 or a < 40:
  print('Такого в табиці немає')
