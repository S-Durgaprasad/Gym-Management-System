from flask import Blueprint, jsonify

from models.dashboard import Dashboard

dashboard_bp = Blueprint("dashboard_bp", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify(Dashboard.get_dashboard())