'''Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä,
nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi
 sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.'''

leiviska = float(input("Anna leiviskät"))
naula = float(input("Anna naulat"))
luoti = float(input("Anna luodit"))

luoticounter= luoti*13.3
naulacounter= naula*(13.3*32)
leiviskacounter= leiviska*(20*13.3*32)

'''print(luoticounter)
print(naulacounter)
print(leiviskacounter)'''

result= leiviskacounter + naulacounter + luoticounter
print(result)
kg = int(result/1000)
g= round(result % 1000, 2)

print(kg)
print(g)

print("Massa nykymittojen mukaan:" +"\n" + str(kg) + " kilogrammaa ja " + str(g) + " grammaa.")