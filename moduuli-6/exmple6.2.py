'''Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan
maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.'''

import random

def fc_get_number(sides):
    sides = int(sides)
    result= random.randint(1, sides)
    return result
    #print(f"tämä on yksi nopan heitto: {random.randint(0, 6)}")

user_input = int(input("Anna nopan tahkojen määrä"))
result = fc_get_number(user_input)
while result != user_input:
    print(result)
    result = fc_get_number(user_input)
while result == user_input:
    print(f"more than {user_input}")
    break