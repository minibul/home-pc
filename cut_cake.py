def cut_cake(parts):
	try:
		return 1 / int(parts)
	except (ZeroDivisionError, TypeError, ValueError):
		return 'Вы что, с ума посходили?'


cake = cut_cake([1 ,2, 5])
# print(cake)


def do_something(x):
	try:
		print(x)
	except:
		print('Пока!')


x = 0
while x < 10:
	do_something(x)
x += 1