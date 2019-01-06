# Glossary
python_words = {'dictionary' : 'a set of unordered keys and values',
		'set' : 'a set of ordered keys and values',
		'boolean' : 'a value or expression that is either true or false',
		'tuple' : 'a list whose contents cannot be changed',
		'string' : 'a series of characters' }

for keyword, definition in python_words.items():
	print keyword.capitalize(), "-", definition.capitalize()
