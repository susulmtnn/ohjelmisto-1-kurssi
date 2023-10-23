'''Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa
ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin. Uuden auton
 nopeus ja kuljetut matka on asetettava automaattisesti nollaksi. Kirjoita pääohjelma,
 jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h). Tulosta pääohjelmassa
 sen jälkeen luodun auton kaikki ominaisuudet'''

class Auto:
    def __init__(self, registerplate, maxi_speed):
        self.cur_speed = 0
        self.km_travelled = 0
        self.registerplate = registerplate
        self.maxi_speed = maxi_speed
        #print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def initialize_auto(self):
        print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

auto1 = Auto("ABC-123", 142)
auto1.initialize_auto()