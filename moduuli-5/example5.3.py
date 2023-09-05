'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.'''

user_input= int(input("Anna kokonaisluku"))

isPrime= True

for x in range(2, user_input):
    if user_input % x ==0:
        isPrime = False
        #print("Luku ei ole alkuluku")
#print("Luku on alkuluku")
if isPrime:
    print(f"Luku {user_input} on alkuluku")
else:
    print("Ei ole alkuluku")