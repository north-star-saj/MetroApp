from flask import (
    Flask,
    render_template,
)
import requests

app = Flask(__name__)

data = [
    {
        "bus_route_id": "1",
        "bus_route": "route1",
    },
    {"bus_route_id": "2", "bus_route": "route2"},
]


@app.route("/")
def index():
    data = get_routes()
    return render_template("index.html", busroutes=data)


def get_routes():
    r = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    return r.json()
