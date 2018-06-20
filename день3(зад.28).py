mport datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




t = open('samp.txt', 'r')
for i in range(10):
    print(t.readline())

t.close()


