'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan
 kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun
  ident-sarakkeeseen.'''

import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user= 'suvi',
    password = 'HarmaaPoyta123',
    autocommit = True
    )

def fc_get_airportname_and_region(ICAO):
    cursor= connection.cursor()
    sql= f"select name, municipality from airport WHERE ident='{ICAO}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        return str(result)


ICAO = input("Anna lentokentän ICAO-koodi:")
result =fc_get_airportname_and_region(ICAO)
print(result)