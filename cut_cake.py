def cut_cake(parts):
	try:
		return 1 / int(parts)
	except ZeroDivisionError:
		return 'Вы что, с ума посходили?'

cake = cut_cake(0)
print(cake)