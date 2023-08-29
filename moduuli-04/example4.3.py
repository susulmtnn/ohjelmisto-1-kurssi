'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.'''

unum1= input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki")
num2 = float(num1)
num3= float(num1)

while num1 != " ":
    num1 =float(num1)
    while num1 <= num2:
        num2 = num1
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
    while num1 >= num3:
        num3 = num1
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
    else:
         num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))
while user_output == " ":
        print("pienin luku:" + num1 + "ja suurin luku:" + num2)
        num1 = float(input("anna luku, mikäli haluat lopettaa, anna tyhjä lopetusmerkki"))