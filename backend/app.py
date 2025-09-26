from flask import Flask, send_from_directory
from flask_cors import CORS 
import os 

app = Flask(__name__)
CORS(app)

@app.route("/geojson")
def geojson():
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), "..", "geojson"),
        "beograd_opstine.geojson"
    )

if __name__ == "__main__":
    app.run(debug=True)