'''Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
 Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena
 on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa
 parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa
 kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot
 yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
 Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen
 matkamittarilukemat.'''

class Auto:
    def __init__(self, registerplate, maxi_speed):
        self.cur_speed = 0
        self.km_travelled = 0
        self.registerplate = registerplate
        self.maxi_speed = maxi_speed
        #print(f"New car. Register plate: {self.registerplate}. Current speed: {self.cur_speed} km/h. Max speed: {self.maxi_speed}")

    def kulje(self, hr_nbr):
        travelled = self.km_travelled + (self.maxi_speed * hr_nbr)
        self.km_travelled = travelled
        print(travelled)

class Sähkö_auto(Auto):
    def __init__(self, registerplate, maxi_speed, kWh):
        super().__init__(registerplate, maxi_speed)
        self.kWh = kWh


class Polttomoottori_auto(Auto):
    def __init__(self, registerplate, maxi_speed, litres):
        super().__init__(registerplate, maxi_speed)
        self.litres = litres

sähkö_auto = Sähkö_auto("ABC-15", 180, 52.5)
polttomoottori_auto = Polttomoottori_auto("ACD-123", 165, 32.3)
sähkö_auto.kulje(3)
polttomoottori_auto.kulje(3)