import datetime
def printTimeStamp(name):
    print('Овчарнеко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

sequence = [3, 9, 13, 15, 17]
for num in sequence:
  print(("x"*num).center(20))
for num in reversed(sequence):
  print(("x"*num).center(20))
