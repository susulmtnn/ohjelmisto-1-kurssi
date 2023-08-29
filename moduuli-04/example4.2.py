'''Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
 käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm'''

user_input = float(input("Anna senttimetrimitta."))

while user_input>=0:
    print((str(user_input/2.54)) + " tuumaa.")
    user_input=float(input("Anna senttimetrimitta."))
while user_input<0:
    break