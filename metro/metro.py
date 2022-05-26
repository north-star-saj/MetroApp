from flask import (
    Blueprint,
    Flask,
    jsonify,
    render_template,
)
import requests

bp = Blueprint("metro", __name__)


@bp.route("/")
def index():
    r = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    return render_template("index.html", busroutes=r.json())


@bp.route("/busroute/<id>")
def get_direction(id):
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/directions/{id}")
    return jsonify(r.json())


@bp.route("/stops/<route_id>/<direction_id>")
def get_routes(route_id, direction_id):
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/stops/{route_id}/{direction_id}")
    return jsonify(r.json())
