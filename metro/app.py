from flask import (
    Flask,
    jsonify,
    render_template,
)
import requests

app = Flask(__name__)


@app.route("/")
def index():
    data = get_routes()
    return render_template("index.html", busroutes=data)


def get_routes():
    r = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    return r.json()


@app.route("/busroute/<id>")
def get_direction(id):
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/directions/{id}")
    return jsonify(r.json())
