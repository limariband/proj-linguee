from linguee import Linguee
from anki import Anki

def main(word):
    obj = Linguee(word)
    ank = Anki()

    stt = obj.request()

    if stt:
        lst = obj.list()

    if len(lst) > 0:
        for x,y in lst:
            ank.target, ank.source = x, y
            ank.card()
            r = ank.insert()

            if r > 0: 
                print (r)

