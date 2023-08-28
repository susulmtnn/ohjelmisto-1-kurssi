'''Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
'''

gender = str(input("Syötä sukupuoli muodossa 'nainen' tai 'mies'"))
val = int(input("Syötä hemoglobiiniarvo"))

if gender == "nainen" or gender == "Nainen":
    if 117 <= val <= 175:
        print("Normal")
    elif val <117:
        print("Alhainen")
    else:
        print("Korkea")
elif gender == "mies" or gender == "Mies":
    if 134 <= val <= 195:
        print("Normal")
    elif val < 134:
        print("Alhainen")
    else:
        print("Korkea")