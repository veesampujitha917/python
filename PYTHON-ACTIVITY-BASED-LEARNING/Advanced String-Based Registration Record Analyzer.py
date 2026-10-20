
def registration_record_analyzer():
    records = [
        "R001|Anaya Rao|anaya@example.com|9876543210|20",
        "R002|Vikram Shah|vikram@example.com|9876543211|21",
        "R003|Anaya Rao|anaya@example.com|9876543210|20",
        "R004|Li|bad-email|12345|17",
        "R005|Meera Nair|meera@example.com|9876543212|22",
        "R006|Broken Record"
    ]

    seen_ids = set()
    seen_emails = set()

    for record in records:
        print("\nRecord:", record)
        parts = record.split("|")
        errors = []

        if len(parts) != 5:
            errors.append("Incorrect number of fields")
        else:
            reg_id, name, email, phone, age_text = [
                p.strip() for p in parts
            ]

            if not 4 <= len(reg_id) <= 8:
                errors.append("Invalid registration ID")
            if not 2 <= len(name) <= 40:
                errors.append("Invalid name")
            if "@" not in email or "." not in email.split("@")[-1]:
                errors.append("Invalid email")
            if not (phone.isdigit() and len(phone) == 10):
                errors.append("Invalid phone number")

            try:
                age = int(age_text)
                if not 16 <= age <= 100:
                    errors.append("Age out of range")
            except ValueError:
                errors.append("Invalid age")

            if reg_id in seen_ids:
                errors.append("Duplicate registration ID")
            if email in seen_emails:
                errors.append("Duplicate email")

            seen_ids.add(reg_id)
            seen_emails.add(email)

        print("Status:", "VALID" if not errors else "INVALID")
        print("Errors:", errors if errors else "None")


if __name__ == "__main__":
    registration_record_analyzer()
