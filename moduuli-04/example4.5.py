'''Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).'''

user = input("Anna käyttäjätunnus")
password = input("Anna salasana")

counter=int(1)

while counter < int(5):
    print(counter)
    while user != "python" and counter < int(5):
        counter = counter+1
        print(counter)
        user = input("Anna käyttäjätunnus")
        password = input("Anna salasana")
    while password != "rules" and counter < int(5):
        counter = counter + 1
        user = input("Anna käyttäjätunnus")
        password = input("Anna salasana")
        print(counter)
    while user == "python" and password == "rules" and counter < int(5):
        print("Tervetuloa")
        break
    while counter == 5:
        print("Pääsy evätty")
        break
