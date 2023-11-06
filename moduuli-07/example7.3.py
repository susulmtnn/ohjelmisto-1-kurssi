'''Kirjoita ohjelma lentoasematietojen hakemiseksi ja
tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä
syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai
 lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma
 kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä
 valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan
 lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
 Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen
  asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä
   tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
    Löydät koodeja helposti selaimen avulla.)'''

user_input = input("Haluatko 'syöttää uuden' lentoaseman, 'hakea jo syötetyn' lentoaseman tiedot vai 'lopettaa?'")

airports = {}

def fc_add_icao_and_name(ICAO, name):
    airports1 = {}
    airports1[ICAO] = {"name"}
    return airports1



if user_input:
    if user_input == "syöttää uuden":
        user_new_input = input("Anna ICAO koodi")
        koodi = user_new_input
        user_new_input = input("Anna nimi")
        nimi = user_new_input
        airports[koodi]= nimi
        print(airports)
    elif user_input == "hakea jo syötetyn":
        user_new_input = input("Anna ICAO-koodi")
        if user_new_input in airports:
            print(f"Lentokentän {user_new_input} nimi on {airports[user_new_input]}")
    elif user_input == "lopettaa":
        print("Lopetetaan")
    else:
        user_input = input(
            "Haluatko 'syöttää uuden' lentoaseman, 'hakea jo syötetyn' lentoaseman tiedot vai 'lopettaa?'")


