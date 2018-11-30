year = int(input('Сколько вам лет? : '))

if year >=0 and year <=1:
	print('Вероятней всего вы слишком малы :(')
elif year <=7:
	print('Вы ходите в детский сад!')
elif year <=16:
	print('Вы ходите в школу!')
elif year <=22:
	print('Вы учитесь в институте!')
elif year >=23:
	print('Вы работаете! :(')	