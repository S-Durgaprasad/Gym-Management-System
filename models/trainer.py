from utils.database import get_connection


class Trainer:

    @staticmethod
    def add_trainer(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO trainers(
            full_name,
            specialization,
            phone,
            email,
            experience,
            salary,
            joining_date
        )
        VALUES(?,?,?,?,?,?,?)
        """, (
            data["full_name"],
            data["specialization"],
            data["phone"],
            data["email"],
            data["experience"],
            data["salary"],
            data["joining_date"]
        ))

        conn.commit()

        trainer_id = cursor.lastrowid

        conn.close()

        return trainer_id

    @staticmethod
    def get_all_trainers():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM trainers")

        trainers = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return trainers

    @staticmethod
    def get_trainer(trainer_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM trainers WHERE trainer_id=?",
            (trainer_id,)
        )

        trainer = cursor.fetchone()

        conn.close()

        if trainer:
            return dict(trainer)

        return None

    @staticmethod
    def update_trainer(trainer_id, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE trainers
        SET
            full_name=?,
            specialization=?,
            phone=?,
            email=?,
            experience=?,
            salary=?,
            joining_date=?
        WHERE trainer_id=?
        """, (
            data["full_name"],
            data["specialization"],
            data["phone"],
            data["email"],
            data["experience"],
            data["salary"],
            data["joining_date"],
            trainer_id
        ))

        conn.commit()

        updated = cursor.rowcount

        conn.close()

        return updated

    @staticmethod
    def delete_trainer(trainer_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM trainers WHERE trainer_id=?",
            (trainer_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        conn.close()

        return deleted