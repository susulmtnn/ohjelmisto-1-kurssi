'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h
 esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy
  viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen
  on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.'''

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = bottom_floor

    def move_up(self):
        self.location += 1
        print(f"You have moved up one floor. Now you're at {self.location}")

    def move_down(self):
        self.location -= 1
        print(f"You have down one floor. Now you're at {self.location}")

    def travel_to_floor(self, target_floor):
        while self.location != target_floor:
            if target_floor > self.location:
                self.move_up()
            elif target_floor < self.location:
                self.move_down()
        else:
            print(f"You have arrived to the target floor: {target_floor}")

hissi = Elevator(1, 12)
hissi.travel_to_floor(5)
hissi.travel_to_floor(1)