import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


n = int(input('Кількість осіб:'))
price_ch = 18
price_vz = 25
r = []
for i in range(0,n):
  c = input('Введите личность:')
  s = int(str(input('Сколько лет?:')))
  template = '{:.' + str(2) + 'f}'
  znishka = sum (r) - sum(r) * 0.10
  if n < 10 and c == 'Дитина' and s in range(0,3):
    print('Безкоштовно')
  elif n < 10 and c == 'Дитина' and s in range(3,12):
    r.append(price_ch)
  elif n < 10 and c == 'Дорослий' and s > 12:
    r.append(price_vz)
  elif n > 10 and c == 'Дитина' and s in range(3,12):
    r.append(price_ch)
    print(price_ch - price_ch * 0.10)
  elif n > 10 and c == 'Дорослий' and s > 12:
    r.append(price_vz - price_vz * 0.10)
print(template.format(sum(r)),'$')



