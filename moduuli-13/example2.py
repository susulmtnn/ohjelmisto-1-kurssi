from flask import Flask, request, Response, render_template
import json
import tietokantahaku

app = Flask(__name__)
app.debug = True
# print(__name__)

@app.route('/')
def get_root():
    return "Moro maailma!"


@app.route('/kenttä/<icao>')
def multiply(icao):

    try:
        kenttä, kaupunki = tietokantahaku.get_ICAO(icao)
        status_code = 200
        response_data = {
            "ICAO": icao,
            "Name": kenttä,
            "Municipality": kaupunki
        }

    except ValueError:
        response_data = {
            "msg": "Virheellinen icao-koodi",
            "input_icao": icao
        }
        status_code = 400


    # convert python dict to json format "manually"
    response_data = json.dumps(response_data)
    # setting up a status code for response needs Response object to be created
    response = Response(response=response_data, status=status_code, mimetype="application/json")
    return response

# https://flask.palletsprojects.com/en/2.3.x/errorhandling/

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    # return Response(response=jsonvast, status=404, mimetype="application/json")
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)