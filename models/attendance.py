from utils.database import get_connection


class Attendance:

    @staticmethod
    def check_in(data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO attendance(
            member_id,
            attendance_date,
            check_in_time,
            check_out_time,
            status
        )
        VALUES (?,?,?,?,?)
        """, (
            data["member_id"],
            data["attendance_date"],
            data["check_in_time"],
            data.get("check_out_time"),
            data.get("status", "Present")
        ))

        conn.commit()

        attendance_id = cursor.lastrowid

        conn.close()

        return attendance_id

    @staticmethod
    def get_all_attendance():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            attendance.*,
            members.full_name
        FROM attendance
        JOIN members
        ON attendance.member_id = members.member_id
        ORDER BY attendance_date DESC
        """)

        records = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return records

    @staticmethod
    def get_member_attendance(member_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM attendance
        WHERE member_id=?
        ORDER BY attendance_date DESC
        """, (member_id,))

        records = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return records

    @staticmethod
    def get_attendance(attendance_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM attendance
            WHERE attendance_id=?
        """, (attendance_id,))

        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)

        return None
    
    @staticmethod
    def update_attendance(attendance_id, data):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE attendance
        SET
            member_id=?,
            attendance_date=?,
            check_in_time=?,
            check_out_time=?,
            status=?,
            workout_completed=?
        WHERE attendance_id=?
        """, (
            data["member_id"],
            data["attendance_date"],
            data["check_in_time"],
            data.get("check_out_time"),
            data["status"],
            data.get("workout_completed", "No"),
            attendance_id
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def complete_workout(attendance_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE attendance
            SET workout_completed = 'Yes'
            WHERE attendance_id = ?
        """, (attendance_id,))

        conn.commit()
        conn.close()

        return True

    @staticmethod
    def delete_attendance(attendance_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM attendance WHERE attendance_id=?",
            (attendance_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        conn.close()

        return deleted