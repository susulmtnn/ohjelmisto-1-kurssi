'''Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
 Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla:
 https://geopy.readthedocs.io/en/stable/. Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
 Kirjoita hakukenttään geopy ja vie asennus loppuun.'''


import mysql.connector


connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user= 'suvi',
    password = 'HarmaaPoyta123',
    autocommit = True
    )

def fc_calculate_distance(icao_airport1, icao_airport2):
    cursor = connection.cursor()
    sql = f"select latitude_deg, longitude_deg from airport WHERE ident='{icao_airport1}' or ident='{icao_airport2}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = tuple(result)
    if result:
        from geopy import distance
        return(distance.distance(result[0:1], result[2:3]).km)

    else:
        return (f"koodia {icao_airport1} tai {icao_airport2} ei löytynyt, yritä uudelleen.")


user_input1 = input("Anna lentokentän 1 ICAO-koodi")
user_input2 = input("Anna lentokentän 2 ICAO-koodi")
final_result = fc_calculate_distance(user_input1, user_input2)
print(f"Etäisyys on {final_result} kilometriä.")
