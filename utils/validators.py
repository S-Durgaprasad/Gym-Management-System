import re


def validate_member(data):
    """
    Validate member input data.
    Returns (True, "") if valid,
    otherwise (False, error_message).
    """

    required_fields = [
        "full_name",
        "age",
        "gender",
        "phone",
        "email",
        "height",
        "weight",
        "trainer_id",
        "membership_id"
    ]

    for field in required_fields:
        if field not in data or str(data[field]).strip() == "":
            return False, f"{field} is required."

    # Age
    try:
        age = int(data["age"])
        if age < 10 or age > 100:
            return False, "Age must be between 10 and 100."
    except ValueError:
        return False, "Age must be a number."

    # Height
    try:
        height = float(data["height"])
        if height <= 0:
            return False, "Height must be greater than 0."
    except ValueError:
        return False, "Invalid height."

    # Weight
    try:
        weight = float(data["weight"])
        if weight <= 0:
            return False, "Weight must be greater than 0."
    except ValueError:
        return False, "Invalid weight."

    # Trainer ID
    try:
        trainer_id = int(data["trainer_id"])
        if trainer_id <= 0:
            return False, "Invalid trainer_id."
    except ValueError:
        return False, "trainer_id must be a number."

    # Membership ID
    try:
        membership_id = int(data["membership_id"])
        if membership_id <= 0:
            return False, "Invalid membership_id."
    except ValueError:
        return False, "membership_id must be a number."

    # Email
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data["email"]):
        return False, "Invalid email address."

    # Phone
    phone_pattern = r'^[0-9]{10}$'
    if not re.match(phone_pattern, data["phone"]):
        return False, "Phone number must contain exactly 10 digits."

    return True, ""

def validate_trainer(data):
    """
    Validate trainer input data.
    Returns (True, "") if valid,
    otherwise (False, error_message).
    """

    import re

    required_fields = [
        "full_name",
        "specialization",
        "phone",
        "email",
        "experience",
        "salary",
        "joining_date"
    ]

    for field in required_fields:
        if field not in data or str(data[field]).strip() == "":
            return False, f"{field} is required."

    # Experience
    try:
        experience = int(data["experience"])
        if experience < 0:
            return False, "Experience cannot be negative."
    except ValueError:
        return False, "Experience must be a number."

    # Salary
    try:
        salary = float(data["salary"])
        if salary < 0:
            return False, "Salary cannot be negative."
    except ValueError:
        return False, "Salary must be a valid number."

    # Email
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, data["email"]):
        return False, "Invalid email address."

    # Phone
    phone_pattern = r'^[0-9]{10}$'
    if not re.match(phone_pattern, data["phone"]):
        return False, "Phone number must contain exactly 10 digits."

    return True, ""

def validate_membership(data):

    required_fields = [
        "plan_name",
        "duration_months",
        "price"
    ]

    for field in required_fields:
        if field not in data or str(data[field]).strip() == "":
            return False, f"{field} is required."

    try:
        duration = int(data["duration_months"])
        if duration <= 0:
            return False, "Duration must be greater than 0."
    except ValueError:
        return False, "Duration must be a valid number."

    try:
        price = float(data["price"])
        if price < 0:
            return False, "Price cannot be negative."
    except ValueError:
        return False, "Price must be a valid number."

    return True, ""

def validate_attendance(data):

    required_fields = [
        "member_id",
        "attendance_date",
        "check_in_time"
    ]

    for field in required_fields:
        if field not in data or str(data[field]).strip() == "":
            return False, f"{field} is required."

    try:
        int(data["member_id"])
    except ValueError:
        return False, "member_id must be a valid integer."

    return True, ""

def validate_payment(data):

    required = [
        "member_id",
        "amount",
        "payment_date",
        "payment_method"
    ]

    for field in required:
        if field not in data:
            return False, f"{field} is required."

    try:
        int(data["member_id"])
    except:
        return False, "Invalid member_id."

    try:
        float(data["amount"])
    except:
        return False, "Invalid amount."

    return True, ""

def validate_workout(data):

    required_fields = [
        "member_id",
        "trainer_id",
        "workout_type",
        "duration",
        "workout_date"
    ]

    for field in required_fields:
        if field not in data or str(data[field]).strip() == "":
            return False, f"{field} is required."

    try:
        duration = int(data["duration"])
        if duration <= 0:
            return False, "Duration must be greater than 0."
    except:
        return False, "Duration must be a valid number."

    return True, "Validation successful."