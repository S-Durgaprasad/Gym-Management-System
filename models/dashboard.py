from utils.database import get_connection


class Dashboard:

    @staticmethod
    def get_dashboard():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM members")
        total_members = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM trainers")
        total_trainers = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM members
            WHERE membership_status='Active'
        """)
        active_memberships = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
            WHERE attendance_date=date('now')
        """)
        today_attendance = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*)
            FROM workouts
        """)
        total_workouts = cursor.fetchone()[0]

        cursor.execute("""
            SELECT IFNULL(SUM(amount),0)
            FROM payments
        """)
        total_revenue = cursor.fetchone()[0]

        cursor.execute("""
            SELECT ROUND(AVG(bmi),2)
            FROM members
        """)
        average_bmi = cursor.fetchone()[0]

        conn.close()

        return {
            "total_members": total_members,
            "total_trainers": total_trainers,
            "active_memberships": active_memberships,
            "today_attendance": today_attendance,
            "total_workouts": total_workouts,
            "total_revenue": total_revenue,
            "average_bmi": average_bmi
        }