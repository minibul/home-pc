def 


first_line = input('Введите ваш password: ') 
second_line = input('Повторите ваш password: ')

if first_line == second_line:
	print(1)

elif first_line >= second_line:
	print(2)

elif first_line != second_line and 'learn':
	print(3)

else:
	print(0)


