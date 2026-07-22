from flask import Blueprint, jsonify

from models.analytics import Analytics

analytics_bp = Blueprint("analytics_bp", __name__)


@analytics_bp.route("/analytics/summary", methods=["GET"])
def analytics_summary():

    summary = Analytics.get_summary()

    return jsonify(summary)

@analytics_bp.route("/analytics/revenue", methods=["GET"])
def analytics_revenue():

    return jsonify(Analytics.get_revenue())


@analytics_bp.route("/analytics/bmi", methods=["GET"])
def analytics_bmi():

    return jsonify(Analytics.get_bmi())


@analytics_bp.route("/analytics/attendance", methods=["GET"])
def analytics_attendance():

    return jsonify(Analytics.get_attendance())