import json

with open('states.json') as f:
	states = json.load(f)

	

for state in states:
	print(state['name'],state['abbreviation'])