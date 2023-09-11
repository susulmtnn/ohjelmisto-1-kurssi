'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan
satunnaisen nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin
 kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.'''

import random

def fc_get_number():
    result= random.randint(1, 6)
    return result
    #print(f"tämä on yksi nopan heitto: {random.randint(0, 6)}")


result = fc_get_number()
while result != 6:
    print(result)
    result = fc_get_number()
while result == 6:
    print("more than 6")
    break