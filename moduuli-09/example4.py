'''Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti
nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
 Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
  "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan
 kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.'''

import numpy as np
import random
class Auto:
    def __init__(self, registerplate, maxi_speed):
        self.cur_speed = 0
        self.km_travelled = 0
        self.registerplate = registerplate
        self.maxi_speed = maxi_speed
        #print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def initialize_auto(self):
        #print(f"This is your car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}. Travelled {self.km_travelled}")
        return(self.registerplate, self.cur_speed)
    def kulje(self, hour_nbr):
        travelled = self.km_travelled + (self.cur_speed * hour_nbr)
        self.km_travelled = travelled

    def accelerate(self, num):
        if self.cur_speed + num < 0:
            self.cur_speed = 0
            #print(self.cur_speed)
        elif self.cur_speed + num <= self.maxi_speed:
            self.cur_speed = self.cur_speed + num
            #print(self.cur_speed)
        else:
            self.cur_speed = self.maxi_speed
            #print(self.maxi_speed)


autot = []
for i in range(10):
    new_auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(new_auto)
while autot[i].km_travelled <1000:
    for auto in autot:
        auto.accelerate(random.randint(-10, 15))
        auto.kulje(1)
        if auto.km_travelled <1000:
            continue
            #print(f"tämän auton nimi: {auto.registerplate} ja nopeus {auto.cur_speed} ja kuljettu matka {auto.km_travelled}")
        else:
            #print(f"finished. The winner is {auto.registerplate} ja nopeus {auto.cur_speed} ja kuljettu matka {auto.km_travelled}")
            print("The race is finished. Here's the final data:")
            for auto in autot:
                print(f"Register plate: {auto.registerplate}. Current speed: {auto.cur_speed}. Max. speed: {auto.maxi_speed}. Km traveled: {auto.km_travelled}")
            quit()
