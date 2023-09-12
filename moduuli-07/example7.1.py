'''Kirjoita ohjelma, joka kysyy käyttäjältä
 kuukauden numeron, jonka jälkeen ohjelma
tulostaa sitä vastaavan vuodenajan (kevät,
 kesä, syksy, talvi). Tallenna ohjelmassasi
kuukausia vastaavat vuodenajat merkkijonoina
monikkotietorakenteeseen. Määritellään kukin
 vuodenaika kolmen kuukauden mittaiseksi siten,
  että joulukuu on ensimmäinen talvikuukausi.'''

user_input = int(input("Anna kuukauden numero"))

vuosi = ("Talvi", "Talvi", "Kevät", "Kevät","Kevät","Kesä","Kesä","Kesä", "Syksy","Syksy","Syksy", "Talvi", "Talvi", "Talvi")

print(vuosi[user_input-1])