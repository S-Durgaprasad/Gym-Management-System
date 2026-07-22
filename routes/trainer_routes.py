from flask import Blueprint, request, jsonify

from models.trainer import Trainer
from utils.validators import validate_trainer
from utils.logger import logger

trainer_bp = Blueprint("trainer_bp", __name__)


# ----------------------------
# Add Trainer
# ----------------------------
@trainer_bp.route("/trainers", methods=["POST"])
def add_trainer():

    try:

        data = request.get_json()

        valid, message = validate_trainer(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        trainer_id = Trainer.add_trainer(data)

        logger.info(f"Trainer Added : {trainer_id}")

        return jsonify({
            "success": True,
            "message": "Trainer added successfully.",
            "trainer_id": trainer_id
        }), 201

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# View All Trainers
# ----------------------------
@trainer_bp.route("/trainers", methods=["GET"])
def get_trainers():

    trainers = Trainer.get_all_trainers()

    return jsonify(trainers), 200


# ----------------------------
# View Trainer by ID
# ----------------------------
@trainer_bp.route("/trainers/<int:trainer_id>", methods=["GET"])
def get_trainer(trainer_id):

    trainer = Trainer.get_trainer(trainer_id)

    if trainer is None:

        return jsonify({
            "success": False,
            "message": "Trainer not found."
        }), 404

    return jsonify(trainer), 200


# ----------------------------
# Update Trainer
# ----------------------------
@trainer_bp.route("/trainers/<int:trainer_id>", methods=["PUT"])
def update_trainer(trainer_id):

    try:

        data = request.get_json()

        valid, message = validate_trainer(data)

        if not valid:
            return jsonify({
                "success": False,
                "message": message
            }), 400

        updated = Trainer.update_trainer(trainer_id, data)

        if updated == 0:

            return jsonify({
                "success": False,
                "message": "Trainer not found."
            }), 404

        logger.info(f"Trainer Updated : {trainer_id}")

        return jsonify({
            "success": True,
            "message": "Trainer updated successfully."
        }), 200

    except Exception as e:

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# ----------------------------
# Delete Trainer
# ----------------------------
@trainer_bp.route("/trainers/<int:trainer_id>", methods=["DELETE"])
def delete_trainer(trainer_id):

    deleted = Trainer.delete_trainer(trainer_id)

    if deleted == 0:

        return jsonify({
            "success": False,
            "message": "Trainer not found."
        }), 404

    logger.info(f"Trainer Deleted : {trainer_id}")

    return jsonify({
        "success": True,
        "message": "Trainer deleted successfully."
    }), 200