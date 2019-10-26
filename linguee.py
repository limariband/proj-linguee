import requests

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
