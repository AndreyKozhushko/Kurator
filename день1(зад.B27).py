import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

n = 10
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
max_width = len(str(m[-1][-1])) + 1
for i in m:
    i = [str(j).rjust(max_width) for j in i]
    print(''.join(i))
