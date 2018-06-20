import datetime
def printTimeStamp(name):
    print('Овчаренко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))




import random
t = open("password.txt", 'r')
text = t.readlines()

password = text[random.randint(0, len(Лох) - 1)].title() + text[random.randint(0, len(text) - 1)]
print(password)
t.close()



