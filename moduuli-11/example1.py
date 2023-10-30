'''Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on
päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
 joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka
 (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.'''

class Julkaisu:
    def __init__(self, name):
        self.name = name

    def tulosta_tiedot(self):
        print(f"Nimi: {self.name}")

class Kirja(Julkaisu):
    def __init__(self, name, writer, page_nbr):
        super().__init__(name)
        self.writer = writer
        self.page_nbr = page_nbr

    def tulosta_tiedot(self):
        print("Kirja")
        super().tulosta_tiedot()
        print(f"Writer: {self.writer}. Page_nrb = {self.page_nbr}")

class Lehti(Julkaisu):
    def __init__(self, name, journalist):
        super().__init__(name)
        self.journalist = journalist

    def tulosta_tiedot(self):
        print("Lehti")
        super().tulosta_tiedot()
        print(f"Writer: {self.journalist}.")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Kirja("Hytti nro 6", "Rosa Liksom", 200)
aku_ankka.tulosta_tiedot()
hytti_no_6.tulosta_tiedot()