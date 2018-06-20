import datetime
def printTimeStamp(name):
    print('Овчарнеко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

a = input('Який день?')
if a == 'Вихідний':
  print('будильник можна не вмикати')
elif a == 'Відпустка':
  print('будильник можна не вмикати')
else:
  print('вмикайте будильник')
