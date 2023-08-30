'''Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin
Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.'''
import random

guess = int(input("Anna luku"))

num = random.randint(1, 10)
print(num)


while guess is not num:
    while guess < num:
        print("Liian pieni arvaus")
        guess = int(input("Anna luku"))
        continue
    while guess > num:
        print("Liian suuri arvaus")
        guess = int(input("Anna luku"))
        continue
while guess == num:
    print("Oikein")
    break
