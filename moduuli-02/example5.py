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
kg = int(result)/2
g= result % 1000

print(kg)
print(g)

'''yhteispainogr = luoticounter+naulacounter+leiviskacounter
print(yhteispainogr)
painolista=list(str(yhteispainogr))
print(painolista)
#print(len(painolista))
length=len(painolista)
print(painolista)
index = painolista.index(".")
#print(index)
if len(painolista)>=3:
    i=0
    #print(painolista[i])
    uusilista=[]
    uusilista.append(painolista[i])
    painolista = painolista.pop()[i]
    i+=1'''
'''else:
    i=0
    print(painolista[i])
    i-=1
print(str(uusilista))'''

'''print(painolista[idx-3] + painolista[idx-2] + painolista[idx-1]+ painolista[idx] + painolista[idx+1])
print(painolista[0] + painolista[1]))'''