import brain as br

import requests
import pandas as pd

from sys import argv
from json import loads

word = argv[1]
deck = argv[2]
model = argv[3]

urla = 'https://linguee-api.herokuapp.com/api?'
urlb = f'https://od-api.oxforddictionaries.com/api/v2/entries/en/{word}'

with open('api-key-oxford.json') as f:
    auth = loads(f.read())

params = {
    'q':word,
    'src':'en',
    'dst':'pt'
}

response = br.make_request(
    urla,
    params=params,
)

df = br.get_examples(response)
if df.empty:
    raise ValueError('DataFrame is empty!')

response = br.make_request(
    urlb,
    headers=auth,
)

pronounce = br.get_pronounce(response)
df['phonetic_spelling'] = pronounce
df['deck'] = deck 
df['model'] = model

try:
    f = df.to_csv(
        'dbase.tsv', 
        sep='\t',
        mode='x',
        index=False,
    )
except FileExistsError:
    f = df.to_csv(
        'dbase.tsv', 
        sep='\t',
        mode='a',
        index=False,
        header=False,
    )