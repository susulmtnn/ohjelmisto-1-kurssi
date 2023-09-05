'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.
'''

import random

user_input = int(input("Anna arpakuutioiden määrä"))

#print(str(user_input) + "this is user input")

sum_count = 0

num1 = 0

for x in range(0, user_input):
    num1 += random.randint(0, 6)
    #print(num1)
    sum_count += num1
else :print(f" tämä on summa {sum_count}")