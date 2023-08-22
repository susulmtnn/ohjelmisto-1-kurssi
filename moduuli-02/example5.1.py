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

result = luoticounter+naulacounter+leiviskacounter


#then we find the length of the number by first making it a string and then calculating length
result=list(str(result))
print(type(result))
print(result)
length=len(result)
print(str(length) + " this is len")

#then we find the delimitator "."
idx = result.index(".")
print(idx)

#then we calculate how many numbers there are after the "."
decimal = (length - idx)
print(str(decimal) + "this is decimal")

#now we can calculate, how many thousands there are:
thousands= length - decimal - 3 -1
print(thousands)

thousandcount= thousands

if thousandcount>0:
    thousandsresults = result[thousands-1]
    thousandcount -= 1
print(thousandsresults)

#then we remove thousands from the original list
if thousands>0:
    result.pop(thousands)
    thousands -= 1
print(result)

#then we join this






'''painolista=list(str(yhteispainogr))
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