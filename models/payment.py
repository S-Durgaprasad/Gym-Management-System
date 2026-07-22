from utils.database import get_connection


class Payment:

    @staticmethod
    def add_payment(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO payments
            (member_id, amount, payment_date,
             payment_method, payment_status, remarks)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["member_id"],
            data["amount"],
            data["payment_date"],
            data["payment_method"],
            data.get("payment_status", "Paid"),
            data.get("remarks")
        ))

        conn.commit()
        payment_id = cursor.lastrowid
        conn.close()

        return payment_id

    @staticmethod
    def get_all_payments():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.*,
                m.full_name
            FROM payments p
            JOIN members m
            ON p.member_id = m.member_id
            ORDER BY p.payment_date DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    @staticmethod
    def get_member_payments(member_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM payments
            WHERE member_id=?
        """, (member_id,))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]
    
    @staticmethod
    def get_payment(payment_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM payments
            WHERE payment_id=?
        """, (payment_id,))

        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)

        return None

    @staticmethod
    def update_payment(payment_id, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE payments
            SET
                amount=?,
                payment_date=?,
                payment_method=?,
                payment_status=?,
                remarks=?
            WHERE payment_id=?
        """, (
            data["amount"],
            data["payment_date"],
            data["payment_method"],
            data["payment_status"],
            data.get("remarks"),
            payment_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def delete_payment(payment_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM payments WHERE payment_id=?",
            (payment_id,)
        )

        conn.commit()
        conn.close()

    @staticmethod
    def add_payment(data):
        conn = None

        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO payments
                (member_id, amount, payment_date,
                payment_method, payment_status, remarks)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                data["member_id"],
                data["amount"],
                data["payment_date"],
                data["payment_method"],
                data.get("payment_status", "Paid"),
                data.get("remarks")
            ))

            conn.commit()
            return cursor.lastrowid

        except Exception:
            if conn:
                conn.rollback()
            raise

        finally:
            if conn:
                conn.close()