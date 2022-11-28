from functools import reduce
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return reduce(lambda acc, ostos: (acc + ostos.lukumaara()), self._ostokset, 0)

    def hinta(self):
        return reduce(lambda acc, ostos: (acc + ostos.hinta()), self._ostokset, 0)

    def lisaa_tuote(self, lisattava: Tuote):
        olemassaoleva_ostos = next((ostos for ostos in self._ostokset if ostos.tuotteen_nimi() == lisattava.nimi()), None)

        if olemassaoleva_ostos:
            olemassaoleva_ostos.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        olemassaoleva_ostos = next((ostos for ostos in self._ostokset if ostos.tuotteen_nimi() == poistettava.nimi()), None)

        if olemassaoleva_ostos:
            if olemassaoleva_ostos.lukumaara() == 1:
                self._ostokset.remove(olemassaoleva_ostos)
            else:
                olemassaoleva_ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
