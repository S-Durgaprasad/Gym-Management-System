from flask import Blueprint, request, jsonify

from models.member import Member
from utils.validators import validate_member
from utils.logger import logger

member_bp = Blueprint("member_bp", __name__)


# ----------------------------
# Add Member
# ----------------------------
@member_bp.route("/members", methods=["POST"])
def add_member():

    try:

        data = request.get_json()

        valid, message = validate_member(data)

        if not valid:
            logger.warning(message)

            return jsonify({
                "success": False,
                "message": message
            }), 400

        member_id = Member.add_member(data)

        logger.info(f"Member Added Successfully : {member_id}")

        return jsonify({
            "success": True,
            "message": "Member added successfully.",
            "member_id": member_id
        }), 201

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# View All Members
# ----------------------------
@member_bp.route("/members", methods=["GET"])
def get_members():

    members = Member.get_all_members()

    return jsonify(members), 200


# ----------------------------
# View Member by ID
# ----------------------------
@member_bp.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):

    member = Member.get_member(member_id)

    if member is None:

        return jsonify({
            "success": False,
            "message": "Member not found."
        }), 404

    return jsonify(member), 200

# ----------------------------
# Update Member
# ----------------------------
@member_bp.route("/members/<int:member_id>", methods=["PUT"])
def update_member(member_id):

    try:

        data = request.get_json()

        valid, message = validate_member(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        updated = Member.update_member(member_id, data)

        if updated == 0:
            return jsonify({
                "success": False,
                "message": "Member not found."
            }), 404

        logger.info(f"Member Updated : {member_id}")

        return jsonify({
            "success": True,
            "message": "Member updated successfully."
        }), 200

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500

# ----------------------------
# Delete Member
# ----------------------------
@member_bp.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):

    deleted = Member.delete_member(member_id)

    if deleted == 0:

        return jsonify({
            "success": False,
            "message": "Member not found."
        }), 404

    logger.info(f"Member Deleted : {member_id}")

    return jsonify({
        "success": True,
        "message": "Member deleted successfully."
    }), 200