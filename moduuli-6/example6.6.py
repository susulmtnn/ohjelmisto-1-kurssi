'''Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per
neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
 Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.'''

import math
import random

def fc_pizza_price(price1, diameter1, price2, diameter2):
    price1 = float(price1)
    diameter1 = float(diameter1)
    price2 = float(price2)
    diameter2= float(diameter2)
    pi1 = math.pi
    final_price1 = (pi1/4)*(diameter1**2)*price1
    final_price2= (pi1/4)*(diameter2**2)*price2
    if final_price1 > final_price2:
        return f"toka pitsa hinnalla {final_price2} e\m^2"
    elif final_price2 > final_price1:
        return f"eka pitsa hinnalla {final_price1} e\m^2"
    else:
        return f" molemmat pitsat hinnalla {final_price1}  e\m^2"


def main():
    user_input1 = input("Anna ensimmäisen pitsan hinta euroissa.")
    user_input2 = input("Anna ensimmäisen pitsan halkaisija senttimetreissä.")
    user_input3 = input("Anna toisen pitsan hinta euroissa.")
    user_input4 = input("Anna toisen pitsan halkaisija senttimetreissä.")
    print(fc_pizza_price(user_input1, user_input2, user_input3, user_input4))

main()