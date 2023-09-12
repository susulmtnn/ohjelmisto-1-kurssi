'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen
 jälkeen sekä alkuperäisen että karsitun listan.'''

import random

def fc_remove_odd_numbers(lista):
    lista1 = lista
    lista2 = []
    for i in lista:
            if i % 2 == 0:
                lista2.append(i)
            else: continue
    return lista2


def main():
    lista = random.sample(range(10, 30), 5)
    #print(lista)
    fc_remove_odd_numbers(lista)
    print(f"tässä alkuperäinen lista {lista}. Tässä toinen lista {fc_remove_odd_numbers(lista)}")


main()
