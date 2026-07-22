import sqlite3
import os

DATABASE = "data/gym.db"


def get_connection():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(
        DATABASE,
        timeout=30,
        check_same_thread=False
    )

    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def initialize_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # Trainers
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trainers(
        trainer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        phone TEXT UNIQUE,
        email TEXT UNIQUE,
        experience INTEGER,
        salary REAL,
        joining_date TEXT
    )
    """)

    # ==========================
    # Membership Plans
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memberships(
        membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plan_name TEXT NOT NULL,
        duration_months INTEGER NOT NULL,
        price REAL NOT NULL,
        description TEXT
    )
    """)
    # ==========================
    # Members
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS members(

        member_id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        age INTEGER NOT NULL,

        gender TEXT NOT NULL,

        dob TEXT,

        phone TEXT UNIQUE,

        email TEXT UNIQUE,

        address TEXT,

        emergency_contact TEXT,

        height REAL,

        weight REAL,

        bmi REAL,

        fitness_goal TEXT,

        medical_conditions TEXT,

        join_date TEXT,

        membership_status TEXT DEFAULT 'Active',

        trainer_id INTEGER,

        membership_id INTEGER,

        FOREIGN KEY(trainer_id)
            REFERENCES trainers(trainer_id),

        FOREIGN KEY(membership_id)
            REFERENCES memberships(membership_id)
    )
    """)

    # ==========================
    # Workouts
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workouts (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        trainer_id INTEGER NOT NULL,
        workout_type TEXT NOT NULL,
        duration INTEGER NOT NULL,
        workout_date TEXT NOT NULL,
        FOREIGN KEY(member_id) REFERENCES members(member_id),
        FOREIGN KEY(trainer_id) REFERENCES trainers(trainer_id)
    );
    """)

    # ==========================
    # Attendance
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        attendance_date TEXT NOT NULL,
        check_in_time TEXT NOT NULL,
        check_out_time TEXT,
        status TEXT DEFAULT 'Present',
        workout_completed TEXT DEFAULT 'No',
        FOREIGN KEY(member_id) REFERENCES members(member_id)
    );
    """)

    # ==========================
    # Payments
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
        payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        member_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        payment_date TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        payment_status TEXT DEFAULT 'Paid',
        remarks TEXT,
        FOREIGN KEY (member_id) REFERENCES members(member_id)
    )
    """)

    conn.commit()
    conn.close()

    print("Database initialized successfully.")