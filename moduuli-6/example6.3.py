'''Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma,
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
 Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
 kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.'''

def fc_gallons_to_litres (gallons):
    return(gallons*3.785)

def main():
    user_input = float(input("Anna bensiinin määrä galloneina"))
    result = fc_gallons_to_litres(user_input)
    print(result)

main()