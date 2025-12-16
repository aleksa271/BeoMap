from flask import Flask, jsonify, send_file, request
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
        "ZEMUN": {"temp": 19, "air": "Dobar", "populacija": 152950, "povrsina" : 15356, "slika" : "/slike/zemun.jpeg", "url": "https://zemun.rs"},
        "NOVI BEOGRAD": {"temp": 20, "air": "Umeren" ,"populacija": 236000, "povrsina" : 4074, "slika" : "/slike/novi_beograd.jpeg", "url": "https://novibeograd.rs"},
        "VRAČAR": {"temp": 22, "air": "Loš", "populacija": 69680, "povrsina" : 292, "slika" :"/slike/vracar.jpeg", "url": "https://vracar.rs"},
        "BARAJEVO": {"temp": 20, "air": "Umeren", "populacija": 25000, "povrsina" : 21312, "slika" :"/slike/barajevo.jpeg", "url": "https://barajevo.bg.ls.gov.rs/"},
        "VOŽDOVAC": {"temp": 22, "air": "Umeren", "populacija": 167000, "povrsina" : 14864, "slika" : "/slike/vozdovac.jpeg", "url": "https://vozdovac.rs"},
        "GROCKA": {"temp": 22, "air": "Umeren", "populacija": 75466, "povrsina" : 28923, "slika" : "/slike/grocka.jpeg", "url": "https://grocka.rs"},
        "ZVEZDARA": {"temp": 22, "air": "Umeren", "populacija": 150000, "povrsina" : 3165, "slika" : "/slike/zvezdara.jpeg", "url": "https://zvezdara.org.rs"},
        "LAZAREVAC": {"temp": 21, "air": "Umeren", "populacija": 62000, "povrsina" : 38351, "slika" : "/slike/lazarevac.jpeg", "url": "https://lazarevac.rs/"},
        "MLADENOVAC": {"temp": 21, "air": "Umeren", "populacija": 56389, "povrsina" : 33900, "slika" : "/slike/mladenovac.jpeg", "url": "https://mladenovac.rs"},
        "OBRENOVAC": {"temp": 221, "air": "Umeren", "populacija": 75949, "povrsina" : 40995, "slika" : "/slike/obrenovac.jpeg", "url": "https://obrenovac.rs"},
        "PALILULA (BEOGRAD)": {"temp": 21, "air": "Umeren", "populacija": 180000, "povrsina" : 44661, "slika" : "/slike/palilula.jpeg", "url": "https://palilula.org.rs"},
        "RAKOVICA": {"temp": 21, "air": "Umeren", "populacija": 97752, "povrsina" : 3036, "slika" : "/slike/rakovica.jpeg", "url": "https://rakovica.rs"},
        "SAVSKI VENAC": {"temp": 23, "air": "Umeren", "populacija": 47682, "povrsina" : 1400, "slika" : "/slike/savski_venac.jpeg", "url": "https://savskivenac.rs"},
        "SOPOT": {"temp": 24, "air": "Umeren", "populacija": 20527, "povrsina" : 27075, "slika" : "/slike/sopot.jpeg", "url": "https://sopot.org.rs"},
        "STARI GRAD": {"temp": 22, "air": "Umeren", "populacija": 70000, "povrsina" : 698, "slika" : "/slike/stari_grad.jpeg", "url": "https://starigrad.org.rs"},
        "ČUKARICA": {"temp": 22, "air": "Umeren", "populacija": 160000, "povrsina" : 28485, "slika" : "/slike/cukarica.jpeg", "url": "https://cukarica.rs"},
        "SURČIN": {"temp": 20, "air": "Umeren", "populacija": 40000, "povrsina" : 15650, "slika" : "/slike/surcin.jpeg", "url": "https://surcin.rs"}

    })

users = {
    "admin": {"id": 1, "password": "admin123", "name": "Administrator"},
    "user": {"id": 2, "password": "user123", "name": "Korisnik"}
}

favorites = {
    1: [],
    2: []
}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = users.get(data["username"])

    if not user or user["password"] != data["password"]:
        return jsonify({"error": "Greska u logovanju"}), 401
    
    return jsonify({
        "userId": user["id"],
        "name": user["name"]
    })

@app.route("/favorites", methods=["GET"])
def get_favorites():
    user_id = int(request.args.get("userId"))
    return jsonify(favorites[user_id])

@app.route("/favorites", methods=["POST"])
def add_favorite():
    data = request.json
    user_id = data["userId"]
    opstina = data["opstina"]

    if opstina not in favorites[user_id]:
        favorites[user_id].append(opstina)

    return jsonify(favorites[user_id])

if __name__ == "__main__":
    app.run(debug=True)


