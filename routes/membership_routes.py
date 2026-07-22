from flask import Blueprint, request, jsonify

from models.membership import Membership
from utils.validators import validate_membership
from utils.logger import logger

membership_bp = Blueprint("membership_bp", __name__)


# ----------------------------
# Add Membership
# ----------------------------
@membership_bp.route("/memberships", methods=["POST"])
def add_membership():

    try:
        data = request.get_json()

        valid, message = validate_membership(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        membership_id = Membership.add_membership(data)

        logger.info(f"Membership Added : {membership_id}")

        return jsonify({
            "success": True,
            "message": "Membership added successfully.",
            "membership_id": membership_id
        }), 201

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# View All Memberships
# ----------------------------
@membership_bp.route("/memberships", methods=["GET"])
def get_memberships():

    memberships = Membership.get_all_memberships()

    return jsonify(memberships), 200


# ----------------------------
# View Membership by ID
# ----------------------------
@membership_bp.route("/memberships/<int:membership_id>", methods=["GET"])
def get_membership(membership_id):

    membership = Membership.get_membership(membership_id)

    if membership is None:
        return jsonify({
            "success": False,
            "message": "Membership not found."
        }), 404

    return jsonify(membership), 200


# ----------------------------
# Update Membership
# ----------------------------
@membership_bp.route("/memberships/<int:membership_id>", methods=["PUT"])
def update_membership(membership_id):

    try:
        data = request.get_json()

        valid, message = validate_membership(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        updated = Membership.update_membership(membership_id, data)

        if updated == 0:
            return jsonify({
                "success": False,
                "message": "Membership not found."
            }), 404

        logger.info(f"Membership Updated : {membership_id}")

        return jsonify({
            "success": True,
            "message": "Membership updated successfully."
        }), 200

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# Delete Membership
# ----------------------------
@membership_bp.route("/memberships/<int:membership_id>", methods=["DELETE"])
def delete_membership(membership_id):

    deleted = Membership.delete_membership(membership_id)

    if deleted == 0:
        return jsonify({
            "success": False,
            "message": "Membership not found."
        }), 404

    logger.info(f"Membership Deleted : {membership_id}")

    return jsonify({
        "success": True,
        "message": "Membership deleted successfully."
    }), 200