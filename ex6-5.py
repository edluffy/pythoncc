# Rivers
major_rivers = {'nile' : 'egypt',
		'amazon' : 'brazil',
		'mississippi' : 'us',
		'ganges' : 'india',
		'danube' : 'germany'}

for river, country in major_rivers.items():
	print 'The', river.capitalize(), 'runs through',
	if country == 'us':
		print country.upper()
	else:
		print country.capitalize()

