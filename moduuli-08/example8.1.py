import _mysql_connector
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user= 'suvi',
    password = 'HarmaaPoyta123',
    autocommit = True
    )

#cursor = connection.cursor() #palauttaa osoitinobjektin jonka kautta voi syöttää
# sql komentoja
'''
cursor.execute("SELECT iso_country, name, continent FROM country")
result = cursor.fetchone()
print(result)
result = cursor.fetchone()
print(result)
result = cursor.fetchall()
print(cursor.rowcount) #tulosrivin määrä
print(result) #koko tulosjoukko listana
for country in result: #country : tulosjoukon yksi rivi tuplena eli monikkona
    print(f"Maa: {country[1]}, Koodi: {country[0]}")
'''
'''
def fc_get_country_by_iso_code(iso_code):
    cursor = connection.cursor()
    cursor.execute(f"SELECT iso_country, name, continent FROM country WHERE iso_country = '{iso_code}'")
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "No results."

country = fc_get_country_by_iso_code("FI")
print(country)
country = fc_get_country_by_iso_code("SE")
print(country)
country =  fc_get_country_by_iso_code(input("Syötä maakoodi"))
print(country) '''

def fc_update_country_by_iso_code(iso_code, country_name):
    cursor = connection.cursor()
    sql = f"UPDATE country set name='{country_name}' where iso_country= '{iso_code}'"
    cursor.execute(sql)
    if cursor.rowcount > 0:
        return(f"koodi {iso_code} päivitetty, uusi maan nimi: {country_name}")
    else:
        return(f"koodia {iso_code} ei löytynyt, eikä muutoksia tehty.")

country_code = input("Anna muokattava koodi")
new_name = input("Anna maalle uusi nimi")
update_result = fc_update_country_by_iso_code(country_code, new_name)
print(update_result)




    #Mysql geopy = calculating distance