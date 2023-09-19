'''Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa
kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen
osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.'''

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user= 'suvi',
    password = 'HarmaaPoyta123',
    autocommit = True
    )

def fc_get_airport_count_and_airport_type(country_code):
    cursor = connection.cursor()
    sql= f"SELECT type, count(*) from airport where iso_country= '{country_code}' group by type"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return result
    else:
        return (f"koodia {country_code} ei löytynyt, yritä uudelleen.")

user_input = input("Anna maan iso-koodi")
final_result = fc_get_airport_count_and_airport_type(user_input)
print(final_result)



