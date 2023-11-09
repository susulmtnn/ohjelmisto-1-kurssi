'''Toteuta taustapalvelu, joka palauttaa annettua lentokentän
ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi
EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
 Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport",
 "Municipality":"Helsinki"}.'''

import mysql.connector
from flask import Flask, request, Response


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user= 'suvi',
    password = 'HarmaaPoyta123',
    autocommit = True
    )

def get_ICAO(icao):
    cursor = connection.cursor()
    sql = f"SELECT name, municipality from airport where ident= '{icao}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    if result:
        #print(result)
        #print(type(result))
        return result
    else:
        return 'not_found', 'not_found'


