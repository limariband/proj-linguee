import requests
from json import loads

class Linguee:
    def __init__(self, q):
        self.q = q
        self.src = 'en'
        self.dst = 'pt'
        self.__lst = []
        self.__url = 'https://linguee-api.herokuapp.com/api?'

    def request(self):
        r = requests.get(self.__url,
        {'q':self.q, 'src':self.src, 'dst':self.dst})

        if r.status_code == 200:
            self.__jsn = r.json()
            return True
        else:
            print(r.status_code)
            return False

    def linguee(self):
        if 'exact_matches' in self.__jsn:
            for elem in self.__jsn['exact_matches']:

                if 'translations' in elem:
                    for item in elem['translations']:

                        if 'examples' in item:
                            for sentence in item['examples']:

                                yield(sentence['source'], sentence['target'])

    def list(self):
        try:
            self.__lst = [x for x in self.linguee()]
            return self.__lst
        except TypeError:
            return self.__lst

class Oxford:
    def __init__(self, word):
        self.auth()
        self.__url = 'https://od-api.oxforddictionaries.com/api/v2/entries/en/' + word.lower()

    def auth(self):
        f = open('api-key-oxford.json', 'r')
        self.__auth = loads(f.read())
    
    def request(self):
        r = requests.get(self.__url,
        headers = self.__auth)

        if r.status_code == 200:
            self.__jsn = r.json()
            return True
        else:
            print(r.status_code)
            return False
    
    def oxford(self):
        try:
            self.phspl = self.__jsn['results'][0]['lexicalEntries'][0]['pronunciations'][0]['phoneticSpelling']
        except:
            self.phspl = None