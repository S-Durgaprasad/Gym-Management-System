from utils.database import get_connection


class Member:

    @staticmethod
    def calculate_bmi(height, weight):
        """
        Height is stored in centimeters.
        Convert to meters before BMI calculation.
        """
        height = float(height) / 100
        weight = float(weight)

        bmi = weight / (height * height)

        return round(bmi, 2)

    # -----------------------------------
    # Add Member
    # -----------------------------------
    @staticmethod
    def add_member(data):

        conn = get_connection()
        cursor = conn.cursor()

        bmi = Member.calculate_bmi(
            data["height"],
            data["weight"]
        )

        cursor.execute("""
        INSERT INTO members(

            full_name,
            age,
            gender,
            dob,
            phone,
            email,
            address,
            emergency_contact,
            height,
            weight,
            bmi,
            fitness_goal,
            medical_conditions,
            join_date,
            membership_status,
            trainer_id,
            membership_id

        )

        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (

            data["full_name"],
            data["age"],
            data["gender"],
            data.get("dob"),
            data["phone"],
            data["email"],
            data.get("address"),
            data.get("emergency_contact"),
            data["height"],
            data["weight"],
            bmi,
            data.get("fitness_goal"),
            data.get("medical_conditions"),
            data.get("join_date"),
            data.get("membership_status", "Active"),
            data["trainer_id"],
            data["membership_id"]

        ))

        conn.commit()

        member_id = cursor.lastrowid

        conn.close()

        return member_id

    # -----------------------------------
    # View All Members
    # -----------------------------------
    @staticmethod
    def get_all_members():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            m.*,
            t.full_name AS trainer_name,
            ms.plan_name
        FROM members m

        LEFT JOIN trainers t
        ON m.trainer_id = t.trainer_id

        LEFT JOIN memberships ms
        ON m.membership_id = ms.membership_id

        ORDER BY m.member_id
        """)

        members = [dict(row) for row in cursor.fetchall()]

        conn.close()

        return members

    # -----------------------------------
    # View Member by ID
    # -----------------------------------
    @staticmethod
    def get_member(member_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            m.*,
            t.full_name AS trainer_name,
            ms.plan_name
        FROM members m

        LEFT JOIN trainers t
        ON m.trainer_id = t.trainer_id

        LEFT JOIN memberships ms
        ON m.membership_id = ms.membership_id

        WHERE m.member_id = ?
        """, (member_id,))

        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)

        return None

    # -----------------------------------
    # Update Member
    # -----------------------------------
    @staticmethod
    def update_member(member_id, data):

        conn = get_connection()
        cursor = conn.cursor()

        bmi = Member.calculate_bmi(
            data["height"],
            data["weight"]
        )

        cursor.execute("""
        UPDATE members
        SET

            full_name=?,
            age=?,
            gender=?,
            dob=?,
            phone=?,
            email=?,
            address=?,
            emergency_contact=?,
            height=?,
            weight=?,
            bmi=?,
            fitness_goal=?,
            medical_conditions=?,
            join_date=?,
            membership_status=?,
            trainer_id=?,
            membership_id=?

        WHERE member_id=?
        """, (

            data["full_name"],
            data["age"],
            data["gender"],
            data.get("dob"),
            data["phone"],
            data["email"],
            data.get("address"),
            data.get("emergency_contact"),
            data["height"],
            data["weight"],
            bmi,
            data.get("fitness_goal"),
            data.get("medical_conditions"),
            data.get("join_date"),
            data.get("membership_status", "Active"),
            data["trainer_id"],
            data["membership_id"],
            member_id

        ))

        conn.commit()

        updated = cursor.rowcount

        conn.close()

        return updated

    # -----------------------------------
    # Delete Member
    # -----------------------------------
    @staticmethod
    def delete_member(member_id):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM members WHERE member_id=?",
            (member_id,)
        )

        conn.commit()

        deleted = cursor.rowcount

        conn.close()

        return deleted