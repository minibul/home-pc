def fun(first, second):
	
	if type(first) != type('') and type(second) != type(''):
		return(0)
	
	elif first == second:
		return(1)

	elif first >= second:
		return(2)

	elif first != second and first != 'learn':
		return(3)

	else:
		return(0)


first_line = input('Введите ваш password: ') 
second_line = input('Повторите ваш password: ')

res = fun(first_line, second_line)
print(res)