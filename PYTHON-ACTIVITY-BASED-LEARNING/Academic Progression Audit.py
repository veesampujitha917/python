
def academic_progression_audit():
    minimum_mark = 40
    minimum_attendance = 75

    students = [
        {
            "id": "S101", "name": "Asha",
            "marks": {"Python": 78, "Math": 65, "DBMS": 32},
            "attendance": 82, "prerequisites": True
        },
        {
            "id": "S102", "name": "Rahul",
            "marks": {"Python": 55, "Math": 48, "DBMS": 61},
            "attendance": 70, "prerequisites": True
        },
        {
            "id": "S103", "name": "Nina",
            "marks": {"Python": 88, "Math": 74, "DBMS": 81},
            "attendance": 91, "prerequisites": False
        },
        {
            "id": "S104", "name": "Arjun",
            "marks": {"Python": 45, "Math": 41, "DBMS": 43},
            "attendance": 80, "prerequisites": True
        },
    ]

    for student in students:
        issues = []

        failed = [
            subject for subject, mark in student["marks"].items()
            if mark < minimum_mark
        ]

        if failed:
            issues.append("Failed subjects: " + ", ".join(failed))

        if student["attendance"] < minimum_attendance:
            issues.append("Attendance below minimum")

        if not student["prerequisites"]:
            issues.append("Prerequisites incomplete")

        average = sum(student["marks"].values()) / len(student["marks"])

        print(f"\n{student['id']} - {student['name']}")
        print(f"Average marks: {average:.1f}%")
        print(f"Attendance: {student['attendance']}%")
        print("Eligibility:", "ELIGIBLE" if not issues else "NOT ELIGIBLE")
        print("Requirements:", "; ".join(issues) if issues else "None")


if __name__ == "__main__":
    academic_progression_audit()
