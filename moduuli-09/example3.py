'''Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
 Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
 tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
 Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.'''

class Auto:
    def __init__(self, registerplate, maxi_speed):
        self.cur_speed = 60
        self.km_travelled = 2000
        self.registerplate = registerplate
        self.maxi_speed = maxi_speed
        #print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def initialize_auto(self):
        print(f"This is your car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}. Travelled {self.km_travelled}")

    def kulje(self, hour_nbr):
        travelled = self.km_travelled + (self.cur_speed * hour_nbr)
        self.km_travelled = travelled

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
auto1.kulje(1.5)
auto1.initialize_auto()
