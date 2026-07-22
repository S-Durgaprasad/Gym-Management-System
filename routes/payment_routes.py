from flask import Blueprint, request, jsonify

from models.payment import Payment
from utils.validators import validate_payment

payment_bp = Blueprint("payment_bp", __name__)


@payment_bp.route("/payments", methods=["POST"])
def add_payment():

    data = request.json

    valid, message = validate_payment(data)

    if not valid:
        return jsonify({
            "success": False,
            "message": message
        }), 400

    payment_id = Payment.add_payment(data)

    return jsonify({
        "success": True,
        "message": "Payment added successfully.",
        "payment_id": payment_id
    })


@payment_bp.route("/payments", methods=["GET"])
def get_all_payments():

    payments = Payment.get_all_payments()

    return jsonify(payments)


@payment_bp.route("/payments/member/<int:member_id>", methods=["GET"])
def get_member_payments(member_id):

    payments = Payment.get_member_payments(member_id)

    return jsonify(payments)

@payment_bp.route("/payments/<int:payment_id>", methods=["GET"])
def get_payment(payment_id):

    payment = Payment.get_payment(payment_id)

    if payment:
        return jsonify(payment)

    return jsonify({
        "success": False,
        "message": "Payment not found."
    }), 404

@payment_bp.route("/payments/<int:payment_id>", methods=["PUT"])
def update_payment(payment_id):

    data = request.json

    Payment.update_payment(payment_id, data)

    return jsonify({
        "success": True,
        "message": "Payment updated successfully."
    })


@payment_bp.route("/payments/<int:payment_id>", methods=["DELETE"])
def delete_payment(payment_id):

    Payment.delete_payment(payment_id)

    return jsonify({
        "success": True,
        "message": "Payment deleted successfully."
    })