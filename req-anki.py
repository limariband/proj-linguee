# personal modules
import func
# third party modules
import requests
# built-in modules
from json import loads
from sys import argv
		
# anki url
url = 'http://localhost:8765'

# pass file name as argument in console
file_name = argv[1]

# open file and pass it as a list
f = open(file_name, 'r').readlines()

# take deck and model name 
for head in f[:2]:
	if head.split('\t')[0].rstrip().lower() == 'deck':
		deck = head.split('\t')[1].rstrip()
	
	elif head.split('\t')[0].rstrip().lower() == 'model':
		model = head.split('\t')[1].rstrip().lower()

# make card and insert into anki
for line in f[:3:-1]:
	card = func.add_note(deck, model, 
		module=line.split('\t')[0].strip().lower(),
		course=line.split('\t')[1].strip().lower(),
		question=line.split('\t')[2].strip().lower(),
		answer=line.split('\t')[3].strip().lower()
		)

	# try insert card
	r = requests.post(url, json=card)

	# transform requisition answer in a dict
	ra = loads(r.text)

	# if deck does not exist then create it and insert card
	if ra['error'] == f'deck was not found: {deck}':
		new_deck = func.create_deck(deck)
		r = requests.post(url, json=new_deck)
		r = requests.post(url, json=card)
	elif ra['error'] == 'cannot create note because it is a duplicate':
		sync = func.sync()
		r = requests.post(url, json=sync)
		exit()

# upload to anki web
sync = func.sync()
r = requests.post(url, json=sync)