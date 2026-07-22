from utils.database import get_connection


class Membership:

    @staticmethod
    def add_membership(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO memberships(
            plan_name,
            duration_months,
            price,
            description
        )
        VALUES (?,?,?,?)
        """, (
            data["plan_name"],
            data["duration_months"],
            data["price"],
            data.get("description")
        ))

        conn.commit()

        membership_id = cursor.lastrowid

        conn.close()

        return membership_id

    @staticmethod
    def get_all_memberships():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM memberships")

        memberships = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return memberships

    @staticmethod
    def get_membership(membership_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM memberships WHERE membership_id=?",
            (membership_id,)
        )

        membership = cursor.fetchone()

        conn.close()

        if membership:
            return dict(membership)

        return None

    @staticmethod
    def update_membership(membership_id, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE memberships
        SET
            plan_name=?,
            duration_months=?,
            price=?,
            description=?
        WHERE membership_id=?
        """, (
            data["plan_name"],
            data["duration_months"],
            data["price"],
            data.get("description"),
            membership_id
        ))

        conn.commit()

        updated = cursor.rowcount

        conn.close()

        return updated

    @staticmethod
    def delete_membership(membership_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM memberships WHERE membership_id=?",
            (membership_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        conn.close()

        return deleted