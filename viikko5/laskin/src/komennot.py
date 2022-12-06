class Miinus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.__sovelluslogiikka = sovelluslogiikka
        self.__lue_syote = lue_syote

    def suorita(self):
        arvo = self.__lue_syote()
        self.__sovelluslogiikka.tulos -= arvo

class Plus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.__sovelluslogiikka = sovelluslogiikka
        self.__lue_syote = lue_syote

    def suorita(self):
        arvo = self.__lue_syote()
        self.__sovelluslogiikka.tulos += arvo

class Nollaa:
    def __init__(self, sovelluslogiikka):
        self.__sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.__sovelluslogiikka.tulos = 0

# class Kumoa:
    # def __init__(self):
        # TODO

    # def suorita(self):
        # TODO
