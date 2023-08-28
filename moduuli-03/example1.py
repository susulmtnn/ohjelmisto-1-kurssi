'''Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla
käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
 Kuha on alamittainen, jos sen pituus on alle 37 cm.
'''

fishlen = float(input("Anna kuhan pituus senttimetreinä"))



if fishlen<32:
    print("Päästä kuha takaisin järveen. Mitasta puuttuu " +str(37-fishlen) + " cm.")

if fishlen>32:
    print("Kuhan pituus on " + str(fishlen) + " cm voit pitää kuhan.")