school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '5a', 'scores': [5,3,1,4,2]}, 
		{'school_class': '6a', 'scores': [1,5,4,5,2]}, 
		{'school_class': '7a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '8a', 'scores': [3,5,5,5,5]}, 
		{'school_class': '9a', 'scores': [3,4,4,5,2]}, 
		{'school_class': '10a', 'scores': [1,4,4,5,3]}]


for ratings in school:
    print(sum(ratings['scores']))


