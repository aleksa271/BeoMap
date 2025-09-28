from flask import Flask, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

GEOJSON_PATH = os.path.join(os.path.dirname(__file__), "../geojson/beograd_opstine.geojson")

@app.route("/api/geojson")
def geojson():
    return send_file(GEOJSON_PATH, mimetype="application/json")

@app.route("/api/data")
def data():
    return jsonify({
        "ZEMUN": {"temp": 19, "air": "Dobar", "populacija": 152950, "povrsina" : 15356, "slika" : "/slike/zemun.jpeg"},
        "NOVI BEOGRAD": {"temp": 20, "air": "Umeren" ,"populacija": 236000, "povrsina" : 4074, "slika" : "/slike/novi_beograd.jpeg"},
        "VRAČAR": {"temp": 22, "air": "Loš", "populacija": 69680, "povrsina" : 292, "slika" :"/slike/vracar.jpeg"},
        "BARAJEVO": {"temp": 20, "air": "Umeren", "populacija": 25000, "povrsina" : 21312, "slika" :"/slike/barajevo.jpeg"},
        "VOŽDOVAC": {"temp": 22, "air": "Umeren", "populacija": 167000, "povrsina" : 14864, "slika" : "/slike/vozdovac.jpeg"},
        "GROCKA": {"temp": 22, "air": "Umeren", "populacija": 75466, "povrsina" : 28923, "slika" : "/slike/grocka.jpeg"},
        "ZVEZDARA": {"temp": 22, "air": "Umeren", "populacija": 150000, "povrsina" : 3165, "slika" : "/slike/zvezdara.jpeg"},
        "LAZAREVAC": {"temp": 21, "air": "Umeren", "populacija": 62000, "povrsina" : 38351, "slika" : "/slike/lazarevac.jpeg"},
        "MLADENOVAC": {"temp": 21, "air": "Umeren", "populacija": 56389, "povrsina" : 33900, "slika" : "/slike/mladenovac.jpeg"},
        "OBRENOVAC": {"temp": 221, "air": "Umeren", "populacija": 75949, "povrsina" : 40995, "slika" : "/slike/obrenovac.jpeg"},
        "PALILULA (BEOGRAD)": {"temp": 21, "air": "Umeren", "populacija": 180000, "povrsina" : 44661, "slika" : "/slike/palilula.jpeg"},
        "RAKOVICA": {"temp": 21, "air": "Umeren", "populacija": 97752, "povrsina" : 3036, "slika" : "/slike/rakovica.jpeg"},
        "SAVSKI VENAC": {"temp": 23, "air": "Umeren", "populacija": 47682, "povrsina" : 1400, "slika" : "/slike/savski_venac.jpeg"},
        "SOPOT": {"temp": 24, "air": "Umeren", "populacija": 20527, "povrsina" : 27075, "slika" : "/slike/sopot.jpeg"},
        "STARI GRAD": {"temp": 22, "air": "Umeren", "populacija": 70000, "povrsina" : 698, "slika" : "/slike/stari_grad.jpeg"},
        "ČUKARICA": {"temp": 22, "air": "Umeren", "populacija": 160000, "povrsina" : 28485, "slika" : "/slike/cukarica.jpeg"},
        "SURČIN": {"temp": 20, "air": "Umeren", "populacija": 40000, "povrsina" : 15650, "slika" : "/slike/surcin.jpeg"}

    })

if __name__ == "__main__":
    app.run(debug=True)
