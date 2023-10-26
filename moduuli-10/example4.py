'''Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on
ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja,
 joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
 Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli
 arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
 Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
  Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen
   aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
    Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen
     sen jälkeen, kun kilpailu on päättynyt.'''

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

class Kilpailu:
    def __init__(self, name, km, autot):
        self.name = name
        self.length_km = km
        self.auto_list = autot

    def one_hour_passed(self):
        for auto in self.auto_list:
            auto.accelerate(random.randint(-10, 15))
            auto.kulje(1)
            #print(f"Register plate: {auto.registerplate}. Current speed: {auto.cur_speed}. Max. speed: {auto.maxi_speed}. Km traveled: {auto.km_travelled}")

    def print_data(self):
        print("Here's the updated data:")
        for auto in self.auto_list:
            print(f"Register plate: {auto.registerplate}. Current speed: {auto.cur_speed}. Max. speed: {auto.maxi_speed}. Km traveled: {auto.km_travelled}")
    def race_over(self):
        for auto in self.auto_list:
            if auto.km_travelled < self.length_km:
                continue
            else:
                return True
        return False



autot = []
for i in range(10):
    new_auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(new_auto)
suuri_romuralli= Kilpailu("Suuri romuralli", 8000, autot)
a =0
while not suuri_romuralli.race_over():
    suuri_romuralli.one_hour_passed()
    a +=1
    if a %10 ==0:
        suuri_romuralli.print_data()
    else:
        continue
else:
    print("The race is finished. Here's the final data:")
    for auto in autot:
        print(f"Register plate: {auto.registerplate}. Current speed: {auto.cur_speed}. Max. speed: {auto.maxi_speed}. Km traveled: {auto.km_travelled}")
    quit()
