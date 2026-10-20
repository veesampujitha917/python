
def campus_incident_prioritization():
    incidents = [
        ("I101", "Exposed electrical wire", "Laboratory", 5, 3),
        ("I102", "Leaking tap", "Hostel", 2, 8),
        ("I103", "Broken classroom fan", "Classroom", 3, 5),
        ("I104", "Blocked emergency exit", "Library", 5, 2),
        ("I105", "Damaged pathway", "Main entrance", 4, 4),
    ]

    high_risk_locations = {
        "Laboratory", "Library", "Main entrance"
    }

    results = []

    for case_id, issue, location, severity, frequency in incidents:
        bonus = 3 if location in high_risk_locations else 0
        score = severity * 10 + frequency * 2 + bonus
        results.append(
            (score, case_id, issue, location, severity, frequency)
        )

    results.sort(reverse=True)

    print("Priority order:")
    for score, case_id, issue, location, severity, frequency in results:
        if score >= 55:
            level = "URGENT"
        elif score >= 40:
            level = "HIGH"
        else:
            level = "NORMAL"

        print(
            f"{case_id} | {issue} | {location} | "
            f"Severity {severity} | Reports {frequency} | "
            f"Score {score} | {level}"
        )


if __name__ == "__main__":
    campus_incident_prioritization()
