'''Toteuta Flask-taustapalvelu, joka ilmoittaa,
 onko parametrina saatu luku alkuluku vai ei. Hyödynnä
 toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
  Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
   http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa:
 {"Number":31, "isPrime":true}.'''

from flask import Flask, request, Response
import json

app = Flask(__name__)

#I found a nicer way to check isPrime: https://en.wikipedia.org/wiki/Primality_test
@app.route('/alkuluku/<num>')
def get_alkuluku(num):
    num = int(num)
    if num == 1:
        isPrime = False
        result ={"Number": num, "isPrime" : isPrime}
        return result
    i=2
    while i*i <=num:
        if num % i == 0:
            isPrime = False
            result ={"Number": num, "isPrime" : isPrime}
            return result
        i+=1
    isPrime = True
    result = {"Number": num, "isPrime": isPrime}
    return result



if __name__ == '__main__':
    app.run(use_reloader=True, host= '127.0.0.1', port=3000)
