'''Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden
 muutoksen (km/h). Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava
  auto-olion nopeus-ominaisuuden arvoa. Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä
  alentua nollaa pienemmäksi. Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
   sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus
   määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä
   päivittää.'''

class Auto:
    def __init__(self, registerplate, maxi_speed):
        self.cur_speed = 0
        self.km_travelled = 0
        self.registerplate = registerplate
        self.maxi_speed = maxi_speed
        #print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def initialize_auto(self):
        print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def accelerate(self, num):
        if self.cur_speed + num < 0:
            self.cur_speed = 0
            print(self.cur_speed)
        elif self.cur_speed + num <= self.maxi_speed:
            self.cur_speed = self.cur_speed + num
            print(self.cur_speed)
        else:
            self.cur_speed = self.maxi_speed
            print(self.maxi_speed)

auto1 = Auto("ABC-123", 142)
auto1.accelerate(30)
auto1.initialize_auto()
auto1.accelerate(70)
auto1.initialize_auto()
auto1.accelerate(50)
auto1.initialize_auto()
auto1.accelerate(-200)
auto1.initialize_auto()