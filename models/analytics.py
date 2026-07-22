from utils.database import get_connection


class Analytics:

    @staticmethod
    def get_summary():

        conn = get_connection()
        cursor = conn.cursor()

        # Total Members
        cursor.execute("SELECT COUNT(*) FROM members")
        total_members = cursor.fetchone()[0]

        # Total Trainers
        cursor.execute("SELECT COUNT(*) FROM trainers")
        total_trainers = cursor.fetchone()[0]

        # Total Membership Plans
        cursor.execute("SELECT COUNT(*) FROM memberships")
        total_memberships = cursor.fetchone()[0]

        # Total Workouts
        cursor.execute("SELECT COUNT(*) FROM workouts")
        total_workouts = cursor.fetchone()[0]

        # Total Payments
        cursor.execute("SELECT COUNT(*) FROM payments")
        total_payments = cursor.fetchone()[0]

        # Total Revenue
        cursor.execute("""
            SELECT IFNULL(SUM(amount),0)
            FROM payments
        """)
        total_revenue = cursor.fetchone()[0]

        # Average BMI
        cursor.execute("""
            SELECT ROUND(AVG(bmi),2)
            FROM members
        """)
        average_bmi = cursor.fetchone()[0]

        conn.close()

        return {
            "total_members": total_members,
            "total_trainers": total_trainers,
            "total_memberships": total_memberships,
            "total_workouts": total_workouts,
            "total_payments": total_payments,
            "total_revenue": total_revenue,
            "average_bmi": average_bmi
        }
    
    @staticmethod
    def get_revenue():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_payments,
                IFNULL(SUM(amount),0) AS total_revenue,
                ROUND(IFNULL(AVG(amount),0),2) AS average_payment
            FROM payments
        """)

        revenue = dict(cursor.fetchone())

        conn.close()

        return revenue
    
    @staticmethod
    def get_bmi():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                ROUND(MIN(bmi),2) AS minimum_bmi,
                ROUND(MAX(bmi),2) AS maximum_bmi,
                ROUND(AVG(bmi),2) AS average_bmi
            FROM members
        """)

        bmi = dict(cursor.fetchone())

        conn.close()

        return bmi
    
    @staticmethod
    def get_attendance():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_attendance,
                SUM(CASE
                        WHEN status='Present'
                        THEN 1
                        ELSE 0
                    END) AS present_days
            FROM attendance
        """)

        attendance = dict(cursor.fetchone())

        conn.close()

        return attendance
    
    