'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
argumentiksi reverse=True.'''


user_input = input("Anna lukuja. Jos haluat tulostaa viisi suurinta, anna tyhjä")

lista = []

while user_input != "":
    lista.append(int(user_input))
    user_input = input("Anna lukuja. Jos haluat tulostaa viisi suurinta, anna enter")
lista.sort(reverse=True)
print(lista[0:5])
