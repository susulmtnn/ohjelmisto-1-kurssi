'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma
 palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.'''

import random

def fc_sum_it(lista):
    return sum(lista)

def main():
    lista= random.sample(range(10, 30), 5)
    #print(lista)
    print(fc_sum_it(lista))

main()
