'''Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
 tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
 Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.'''

hytclas = input("Syötä hyttiluokka")

if hytclas == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytclas == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytclas == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytclas == "C":
    print("B on ikkunaton hytti autokannen yläpuolella.")
else:
    print("Virheellinen hyttiluokka")