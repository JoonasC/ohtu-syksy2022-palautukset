from functools import reduce
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []

    def tavaroita_korissa(self):
        return reduce(lambda acc, ostos: (acc + ostos.lukumaara()), self.ostokset, 0)

    def hinta(self):
        return reduce(lambda acc, ostos: (acc + ostos.hinta()), self.ostokset, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        olemassaoleva_ostos = next((ostos for ostos in self.ostokset if ostos.tuotteen_nimi() == lisattava.nimi()), None)

        if olemassaoleva_ostos:
            olemassaoleva_ostos.muuta_lukumaaraa(1)
        else:
            self.ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
