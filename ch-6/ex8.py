# Pets
pets = [
	{'type': 'dog', 'owner': 'edward'},
	{'type': 'cat', 'owner': 'the internet'},
	{'type': 'tortoise', 'owner': 'bill'}
]

for pet in pets:
	print pet['owner'].capitalize(), "owns a pet", pet['type']
