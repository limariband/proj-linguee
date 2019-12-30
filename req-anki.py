# personal modules
import func
# third party modules
import requests
import pandas as pd
# built-in modules
from json import loads
from sys import argv
		
# anki url
url = 'http://localhost:8765'

# pass file name as argument in console
file_name = argv[1]

# open file and pass it as a list
# f = open(file_name, 'r').readlines()
df = pd.read_csv(
	'dbase.tsv',
	sep='\t',
)

c = list(
		zip(
			df['source'],
			df['target'],
			df['phonetic_spelling'],
			df['deck'],
			df['model'],
		)
)

for s, t, p, d, m in c[::-1]:
	card = func.add_note(
		d.lower(),
		m.lower(), 
		question=s.lower(),
		answer=t.lower(),
		module=p,
	)

	r = requests.post(url, json=card)
	r = loads(r.text)

	if r['error'] == f'deck was not found: {d}':
		new_deck = func.create_deck(d)
		r = requests.post(url, json=new_deck)
		r = requests.post(url, json=card)
		
	elif r['error'] == 'cannot create note because it is a duplicate':
		sync = func.sync()
		r = requests.post(url, json=sync)
		exit()


# upload to anki web
sync = func.sync()
r = requests.post(url, json=sync)