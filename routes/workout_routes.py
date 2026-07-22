from flask import Blueprint, request, jsonify

from models.workout import Workout
from utils.validators import validate_workout

workout_bp = Blueprint("workout_bp", __name__)


@workout_bp.route("/workouts", methods=["POST"])
def add_workout():

    data = request.json

    valid, message = validate_workout(data)

    if not valid:
        return jsonify({
            "success": False,
            "message": message
        }), 400

    workout_id = Workout.add_workout(data)

    return jsonify({
        "success": True,
        "message": "Workout assigned successfully.",
        "workout_id": workout_id
    })


@workout_bp.route("/workouts", methods=["GET"])
def get_all_workouts():

    workouts = Workout.get_all_workouts()

    return jsonify(workouts)


@workout_bp.route("/workouts/member/<int:member_id>", methods=["GET"])
def get_member_workouts(member_id):

    workouts = Workout.get_member_workouts(member_id)

    return jsonify(workouts)

@workout_bp.route("/workouts/<int:workout_id>", methods=["GET"])
def get_single_workout(workout_id):

    workout = Workout.get_workout(workout_id)

    if workout:
        return jsonify(workout)

    return jsonify({
        "success": False,
        "message": "Workout not found."
    }), 404

@workout_bp.route("/workouts/<int:workout_id>", methods=["PUT"])
def update_workout(workout_id):

    data = request.json

    updated = Workout.update_workout(workout_id, data)

    if updated == 0:
        return jsonify({
            "success": False,
            "message": "Workout not found."
        }), 404

    return jsonify({
        "success": True,
        "message": "Workout updated successfully."
    })


@workout_bp.route("/workouts/<int:workout_id>", methods=["DELETE"])
def delete_workout(workout_id):

    deleted = Workout.delete_workout(workout_id)

    if deleted == 0:
        return jsonify({
            "success": False,
            "message": "Workout not found."
        }), 404

    return jsonify({
        "success": True,
        "message": "Workout deleted successfully."
    })