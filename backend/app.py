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
        "Zemun": {"temp": 22, "air": "Dobar"},
        "Novi Beograd": {"temp": 23, "air": "Umeren"},
        "Vračar": {"temp": 25, "air": "Loš"}
    })

if __name__ == "__main__":
    app.run(debug=True)
