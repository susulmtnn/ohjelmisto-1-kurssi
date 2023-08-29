'''Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
 Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia
 myös neljälläsadalla.'''

user_input = int(input("Anna vuosiluku"))

if user_input%100 != 0 and user_input%4 == 0:
    print("karkausvuosi")
elif user_input%4 == 0 and user_input%400==0:
    #if user_input%400==0:
    print("karkausvuosi")
else:
    print("ei karkausvuosi")