# personal modules
import linguee as lg

# third party modules
import requests

# built-in modules
from sys import argv
from json import loads

# take word from argument
w = argv[1] 

# url linguee, oxf
ul = 'https://linguee-api.herokuapp.com/api?'
uo = 'https://od-api.oxforddictionaries.com/api/v2/entries/en/'

# take oxford api key 
f = open('api-key-oxford.json', 'r')
auth = loads(f.read())

# request to linguee api
# if status != 200 exit script
params = {'q':w, 'src':'en', 'dst':'pt'}
try:
    r = requests.get(ul, params=params)
    r.raise_for_status()
except:
    exit(r.status_code)

jlinguee = r.json()

# search in response
rp = lg.search(jlinguee)

# request to oxford api
# if status != 200 exit script
url = uo + w
try:
    r = requests.get(url , headers=auth)
    r.raise_for_status()
except:
    exit(r.status_code)

joxford = r.json()

# take pronunciation
pron = lg.pronunc(joxford)

# verify if the file exist if does not create it and write a head
try:
    file_tsv = open('anki.tsv', 'x')
except FileExistsError:
    file_tsv = open('anki.tsv', 'a')
else:
    file_tsv.write(
        f'Deck\tEnglish\n'\
        f'Model\tlang\n'\
        f'Pronounce\t\tTarget\tSource\n'\
        )
finally:
    for elem in rp:
        file_tsv.write(f'{pron}\t\t{elem[0]}\t{elem[1]}\n')
    file_tsv.close()

with open('req.tsv', 'w', encoding='utf-8') as f:
    
    f.write(
        f'Deck\tEnglish\n'\
        f'Model\tlang\n'\
        f'Pronounce\t\tTarget\tSource\n'\
        )

    for elem in rp:
        f.write(f'{pron}\t\t{elem[0]}\t{elem[1]}\n')
