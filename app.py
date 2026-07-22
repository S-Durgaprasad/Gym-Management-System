from flask import Flask
from flask import Flask, render_template
from flask import render_template

from utils.database import initialize_database

from routes.member_routes import member_bp
from routes.trainer_routes import trainer_bp
from routes.membership_routes import membership_bp
from routes.attendance_routes import attendance_bp
from routes.payment_routes import payment_bp
from routes.workout_routes import workout_bp
from routes.analytics_routes import analytics_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)

initialize_database()

app.register_blueprint(member_bp)
app.register_blueprint(trainer_bp)
app.register_blueprint(membership_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(workout_bp)
app.register_blueprint(analytics_bp)
app.register_blueprint(dashboard_bp)

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/members-page")
def members_page():
    return render_template("members.html")

@app.route("/trainers-page")
def trainers_page():
    return render_template("trainers.html")


@app.route("/memberships-page")
def memberships_page():
    return render_template("memberships.html")


@app.route("/attendance-page")
def attendance_page():
    return render_template("attendance.html")


@app.route("/payments-page")
def payments_page():
    return render_template("payments.html")


@app.route("/workouts-page")
def workouts_page():
    return render_template("workouts.html")


@app.route("/analytics-page")
def analytics_page():
    return render_template("analytics.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
