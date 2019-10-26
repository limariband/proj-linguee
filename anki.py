import requests

class Anki:
    def __init__(self):
        self.target = None
        self.source = None
        # self.pronounce = pronounce
        self.__url = 'http://localhost:8765'

    def card(self):
        self.__card = {
            'action': 'addNote',
            'version': 6,
            'params': {
                'note': {
                    'deckName': 'lang',
                    'modelName': 'lang',
                    'fields': {
                        'source': self.target,
                        'target': self.source,
                        # 'pronounce': 'pronounce'
                    },
                    'options': {
                        'allowDuplicate': False
                    },
                    'tags': [
                    ],
                }
            }
        }

    def insert(self):
        r = requests.post(self.__url, json=self.__card)
        if r.text != 'null':
            return r.json()['result']
        else:
            return 0
