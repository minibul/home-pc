school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '5a', 'scores': [5,3,1,4,2]}, 
		{'school_class': '6a', 'scores': [1,5,4,5,2]}, 
		{'school_class': '7a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '8a', 'scores': [3,5,5,5,5]}, 
		{'school_class': '9a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '10a', 'scores': [1,4,4,5,3]},
		{'school_class': '11a', 'scores': [5,4,4,5,5]}
		]


school_rating = 0


for ratings in school:
	sum_items = sum(ratings['scores']) 
	count_items = len(ratings['scores'])
	name_class = ratings['school_class']
	a = sum_items/count_items
	school_rating = a + school_rating
	print('Средний балл в классе: ' + name_class, a)


print('Средний балл по всей школе: ' + str(school_rating/len(school)))





