from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
CORS(app)

GEOJSON_PATH = os.path.join(os.path.dirname(__file__), "../geojson/beograd_opstine.geojson")

@app.route("/api/geojson")
def geojson():
    return send_file(GEOJSON_PATH, mimetype="application/json")

""" @app.route("/api/data")
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

    }) """

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    favorites = db.relationship("Favorite", backref="user", lazy=True)

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opstina = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Opstina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    temp = db.Column(db.Float)
    air = db.Column(db.String(50))
    populacija = db.Column(db.Integer)
    povrsina = db.Column(db.Integer)
    slika = db.Column(db.String(200))
    url = db.Column(db.String(200))


with app.app_context():
    db.create_all()

    if not User.query.first():
        db.session.add_all([
            User(username="admin", password="admin123", name="Administrator"),
            User(username="user", password="user123", name="Korisnik")
        ])
        db.session.commit()

    if not Opstina.query.first():
        opstine = {
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
        }

        for name, data in opstine.items():
            db.session.add(Opstina(name=name, **data))
        
        db.session.commit()

@app.route("/api/data")
def data():
    opstine = Opstina.query.all()
    return jsonify({
        o.name: {
            "temp": o.temp,
            "air": o.air,
            "populacija": o.populacija,
            "povrsina": o.povrsina,
            "slika": o.slika,
            "url": o.url
        } for o in opstine
    })

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or user.password != data["password"]:
        return jsonify({"error": "Pogresan login"}), 401
    
    return jsonify({
        "userId": user.id,
        "name": user.name
    })

@app.route("/favorites", methods=["GET"])
def get_favorites():
    user_id = int(request.args.get("userId"))
    favs = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([f.opstina  for f in favs])

@app.route("/favorites", methods=["POST"])
def add_favorite():
    data = request.json
    opstina_name = data["opstina"]

    exists = Favorite.query.filter_by(
        user_id=data["userId"],
        opstina=opstina_name
    ).first()

    
    if not exists:
        db.session.add(Favorite(
            user_id=data["userId"],
            opstina=opstina_name
        ))
        db.session.commit()
    
    favs = Favorite.query.filter_by(user_id=data["userId"]).all()
    return jsonify([f.opstina for f in favs])

@app.route("/api/debug")
def debug_db():
    users = [
        {"id": u.id, "username": u.username,"name": u.name}
        for u in User.query.all()
    ]

    opstine = [
        {"id": o.id, "name": o.name, "temp": o.temp, "air": o.air, "populacija": o.populacija, "povrsina": o.povrsina, "slika": o.slika, "url": o.url}
        for o in Opstina.query.all()
    ]

    favorites = [
        {"id": f.id, "user_id": f.user_id, "opstina": f.opstina}
        for f in Favorite.query.all()
    ]

    return jsonify({
        "users": users,
        "opstine": opstine,
        "favorites": favorites
    })

@app.route("/favorites", methods=["DELETE"])
def remove_favorite():
    data = request.json
    user_id = data.get("userId")
    opstina_name = data.get("opstina")

    fav = Favorite.query.filter_by(user_id=user_id, opstina=opstina_name).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()

        favs = Favorite.query.filter_by(user_id=user_id).all()
        return jsonify([f.opstina for f in favs])

if __name__ == "__main__":
    app.run(debug=True)


