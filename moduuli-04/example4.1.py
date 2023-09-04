'''Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000.'''

a=1
while 1<=a<=1000:
    while a%3==0:
        print(a)
        a+= 1
    while a%3!=0:
        a+= 1
print("Kaikki kolmella jaolliset tulostettu")
