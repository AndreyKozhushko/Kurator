import datetime

def printTimeStamp(name):
    print("Овчаренко Иван Кожуко Андрей: " + name)
    print("Час компіляції: " + str(datetime.datetime.now()),"\n")
printTimeStamp("Овчаренко Иван")

x=list(map(str,input()))
myset=set(x)
print(myset)
