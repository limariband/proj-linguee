from linguee import Linguee, Oxford
from anki import Anki

def main(word):
    obj_1 = Linguee(word)
    obj_2 = Oxford(word)
    ank = Anki()

    stt = obj_1.request() and obj_2.request()

    if stt:
        lst, pronounce = obj_1.list(), obj_2.oxford()

    if len(lst) > 0:
        for x,y in lst:
            ank.target, ank.source = x, y
            ank.pronounce = pronounce
            ank.card()
            r = ank.insert()

            if r > 0: 
                print (r)

