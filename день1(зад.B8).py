import datetime
def printTimeStamp(name):
    print('Овчарнеко Иван Кожушко Андрей: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

day = int(input(" День: "))
month = input("Месяц: ")
if month == 'Декабрь':
	astro_sign = 'Стрелец' if (day < 22) else 'Козерог'
elif month == 'Январь':
	astro_sign = 'Козерог' if (day < 20) else 'Водолей'
elif month == 'Февраль':
	astro_sign = 'Водолей' if (day < 19) else 'Рыба'
elif month == 'Март':
	astro_sign = 'Рыба' if (day < 21) else 'Овен'
elif month == 'Апрель':
	astro_sign = 'Овен' if (day < 20) else 'Телец'
elif month == 'Май':
	astro_sign = 'Телец' if (day < 21) else 'Близнеци'
elif month == 'Июнь':
	astro_sign = 'Близнеци' if (day < 21) else 'Рак'
elif month == 'Июль':
	astro_sign = 'Рак' if (day < 23) else 'Лев'
elif month == 'Август':
	astro_sign = 'Лев' if (day < 16) else 'Дева'
elif month == 'Сентябрь':
	astro_sign = 'Дева' if (day < 24) else 'Весы'
elif month == 'Октябрь':
	astro_sign = 'Весы' if (day < 23) else 'Скорпион'
elif month == 'Ноябрь':
	astro_sign = 'Скорпион' if (day < 22) else 'Овен'
print("Знак зодиака :",astro_sign)
