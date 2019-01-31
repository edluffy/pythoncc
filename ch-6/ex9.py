# Favourite Places
favourite_places = {
	'jack': ['new york', 'los angeles', 'atlanta'],
	'john': ['quebec', 'toronto'],
	'james': ['london']
}

for name, places in favourite_places.items():
	
	# if apostrophe is needed
	if name[-1] != 's':
		print name.capitalize() + "'s",
	else:
		print name.capitalize() + "'",
	
	# plural formatting
	if len(places) > 1:
		print "favourite places are:",
	else:
		print "favourite place is:",

	for place in places:
		if (places.index(place) == len(places) - 2): # 2nd last element
			print place.capitalize(), "and",
		elif(places.index(place) == len(places) -1): # last element
			print place.capitalize() + "."
		else:
			print place.capitalize() + ",",
new_list = {
	'list1': ['element1', 'element2', 'element3']
	'list2':
}
