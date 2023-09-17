'''Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
 kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma
  tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi
  ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
   mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen'''

lista2 = []
lista2.append(input("Anna nimi. Jos haluat lopettaa, paina Enter"))
setti = set()

for i in lista2:
    if i != "":
        #print(lista2)
        setti.add(i)
        lista4 = []
        lista4 = list(setti)
        #print(lista4)
        x= int(0)
        while len(lista4) != len(lista2):
            print("Aiemmin syötetty")
            break
        else:
            print("Uusi nimi")
    else:
        lista3 = []
        lista3 = setti
        for i in lista3:
            print(i)
    lista2.append(input("Anna nimi. Jos haluat lopettaa, paina Enter"))



