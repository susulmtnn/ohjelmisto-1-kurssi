'''Kirjoita ohjelma, joka arpoo ja tulostaa kaksi
 erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
Vihje: tutustu random.randint()-funktion käyttöön.
'''

import random
i=0
a=0
str1=""
str2=""
lista2=[]
while i<=2:
    ekakoodi = random.randint(0,9)
    str(ekakoodi)
    str1+=str(ekakoodi) + ", "
    i+=1
while a<=3:
    tokakoodi = random.randint(1, 6)
    str(tokakoodi)
    str2+=str(tokakoodi) + ", "
    a+= 1
str(lista2)
print(str1)
print(str2)
