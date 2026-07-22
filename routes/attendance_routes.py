from flask import Blueprint, request, jsonify

from models.attendance import Attendance
from utils.validators import validate_attendance
from utils.logger import logger

attendance_bp = Blueprint("attendance_bp", __name__)


# ----------------------------
# Member Check-in
# ----------------------------
@attendance_bp.route("/attendance", methods=["POST"])
def check_in():

    try:

        data = request.get_json()

        valid, message = validate_attendance(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        attendance_id = Attendance.check_in(data)

        logger.info(f"Attendance Recorded : {attendance_id}")

        return jsonify({
            "success": True,
            "message": "Attendance recorded successfully.",
            "attendance_id": attendance_id
        }), 201

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# View All Attendance
# ----------------------------
@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():

    records = Attendance.get_all_attendance()

    return jsonify(records), 200


# ----------------------------
# View Attendance by Member
# ----------------------------
@attendance_bp.route("/attendance/member/<int:member_id>", methods=["GET"])
def get_member_attendance(member_id):

    records = Attendance.get_member_attendance(member_id)

    return jsonify(records), 200


@attendance_bp.route("/attendance/<int:attendance_id>", methods=["GET"])
def get_single_attendance(attendance_id):

    record = Attendance.get_attendance(attendance_id)

    if record:
        return jsonify(record)

    return jsonify({
        "success": False,
        "message": "Attendance record not found."
    }), 404


@attendance_bp.route("/attendance/<int:attendance_id>", methods=["PUT"])
def update_attendance(attendance_id):

    data = request.get_json()

    Attendance.update_attendance(attendance_id, data)

    return jsonify({
        "success": True,
        "message": "Attendance updated successfully."
    })

# ----------------------------
# Delete Attendance
# ----------------------------
@attendance_bp.route("/attendance/<int:attendance_id>", methods=["DELETE"])
def delete_attendance(attendance_id):

    deleted = Attendance.delete_attendance(attendance_id)

    if deleted == 0:
        return jsonify({
            "success": False,
            "message": "Attendance record not found."
        }), 404

    logger.info(f"Attendance Deleted : {attendance_id}")

    return jsonify({
        "success": True,
        "message": "Attendance deleted successfully."
    }), 200

@attendance_bp.route("/attendance/complete/<int:attendance_id>", methods=["PUT"])
def complete_workout(attendance_id):

    success = Attendance.complete_workout(attendance_id)

    return jsonify({
        "success": success,
        "message": "Workout marked as completed."
    })