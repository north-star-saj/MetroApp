from flask import (
    Flask,
    jsonify,
    render_template,
)
import requests

app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    return render_template("index.html", busroutes=r.json())


@app.route("/busroute/<id>")
def get_direction(id):
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/directions/{id}")
    return jsonify(r.json())
