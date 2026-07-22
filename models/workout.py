from utils.database import get_connection


class Workout:

    @staticmethod
    def add_workout(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO workouts(
                member_id,
                trainer_id,
                workout_type,
                duration,
                workout_date
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["member_id"],
            data["trainer_id"],
            data["workout_type"],
            data["duration"],
            data["workout_date"]
        ))

        conn.commit()
        workout_id = cursor.lastrowid
        conn.close()

        return workout_id

    @staticmethod
    def get_all_workouts():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                w.workout_id,
                w.member_id,
                m.full_name AS member_name,
                w.trainer_id,
                t.full_name AS trainer_name,
                w.workout_type,
                w.duration,
                w.workout_date
            FROM workouts w
            JOIN members m
                ON w.member_id = m.member_id
            JOIN trainers t
                ON w.trainer_id = t.trainer_id
            ORDER BY w.workout_date DESC
        """)

        workouts = [dict(row) for row in cursor.fetchall()]
        conn.close()

        return workouts

    @staticmethod
    def get_workout(workout_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM workouts
            WHERE workout_id = ?
        """, (workout_id,))

        workout = cursor.fetchone()
        conn.close()

        return dict(workout) if workout else None

    @staticmethod
    def update_workout(workout_id, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE workouts
            SET
                member_id=?,
                trainer_id=?,
                workout_type=?,
                duration=?,
                workout_date=?
            WHERE workout_id=?
        """, (
            data["member_id"],
            data["trainer_id"],
            data["workout_type"],
            data["duration"],
            data["workout_date"],
            workout_id
        ))

        conn.commit()
        updated = cursor.rowcount
        conn.close()

        return updated

    @staticmethod
    def delete_workout(workout_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM workouts WHERE workout_id=?",
            (workout_id,)
        )

        conn.commit()
        deleted = cursor.rowcount
        conn.close()

        return deleted