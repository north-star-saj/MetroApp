"""Core of the application used to get information from the MetroTransit API"""


from flask import (
    Blueprint,
    jsonify,
    render_template,
)
import requests

bp = Blueprint("metro", __name__)


@bp.route("/")
def index():
    """Render the primary page."""
    r = requests.get("https://svc.metrotransit.org/nextripv2/routes")
    return render_template("index.html", busroutes=r.json())


@bp.route("/direction/<id>")
def get_direction(id):
    """Get the applicable directions for the given route."""
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/directions/{id}")
    return jsonify(r.json())


@bp.route("/stops/<route_id>/<direction_id>")
def get_routes(route_id, direction_id):
    """Get the applicable stops for the given route and direction"""
    r = requests.get(f"https://svc.metrotransit.org/nextripv2/stops/{route_id}/{direction_id}")
    return jsonify(r.json())
