
def campus_management_simulation():
    students = [
        {"id": "ST101", "name": "Asha", "attendance": [], "marks": [], "events": []},
        {"id": "ST102", "name": "Ravi", "attendance": [], "marks": [], "events": []},
    ]

    resources = {"Projectors": 5, "Laptops": 10, "Sports Kits": 8}
    events = [("E1", "Tech Fest", 50), ("E2", "Sports Day", 80)]

    while True:
        print("\nSMART CAMPUS MANAGEMENT")
        print("1. List students")
        print("2. Record attendance")
        print("3. Add subject mark")
        print("4. Register student for event")
        print("5. Allocate campus resources")
        print("6. Summary report")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            for student in students:
                print(student["id"], student["name"])
                print("Attendance:", student["attendance"])
                print("Marks:", student["marks"])
                print("Events:", student["events"])

        elif choice == "2":
            sid = input("Student ID: ").strip().upper()
            student = next((s for s in students if s["id"] == sid), None)

            if student:
                status = input("Present or absent (P/A): ").strip().upper()
                if status in ("P", "A"):
                    student["attendance"].append(status)
                    print("Attendance recorded.")
                else:
                    print("Enter P or A.")
            else:
                print("Student not found.")

        elif choice == "3":
            sid = input("Student ID: ").strip().upper()
            student = next((s for s in students if s["id"] == sid), None)

            if student:
                subject = input("Subject name: ").strip()
                try:
                    mark = float(input("Mark (0-100): "))
                    if subject and 0 <= mark <= 100:
                        student["marks"].append((subject, mark))
                        print("Mark saved.")
                    else:
                        print("Invalid subject or mark.")
                except ValueError:
                    print("Enter a numeric mark.")
            else:
                print("Student not found.")

        elif choice == "4":
            sid = input("Student ID: ").strip().upper()
            student = next((s for s in students if s["id"] == sid), None)

            if student:
                print("Available events:", events)
                eid = input("Event ID: ").strip().upper()
                event = next((e for e in events if e[0] == eid), None)

                if event and eid not in student["events"]:
                    student["events"].append(eid)
                    print("Registered for", event[1])
                elif event:
                    print("Already registered.")
                else:
                    print("Event not found.")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Available resources:", resources)
            item = input("Resource name: ").strip().title()

            try:
                amount = int(input("Quantity to allocate: "))

                if item not in resources:
                    print("Unknown resource.")
                elif amount <= 0 or amount > resources[item]:
                    print("Invalid quantity or insufficient stock.")
                else:
                    resources[item] -= amount
                    print("Allocated:", amount, item)
                    print("Remaining:", resources[item])
            except ValueError:
                print("Enter a whole number.")

        elif choice == "6":
            print("\nCAMPUS SUMMARY")

            for student in students:
                total = len(student["attendance"])
                present = student["attendance"].count("P")
                attendance = present / total * 100 if total else 0

                marks = student["marks"]
                average = (
                    sum(mark for subject, mark in marks) / len(marks)
                    if marks else 0
                )

                print(f"\n{student['id']} - {student['name']}")
                print(f"Attendance: {attendance:.1f}%")
                print(f"Average marks: {average:.1f}")
                print("Registered events:", len(student["events"]))

            print("Remaining resources:", resources)

        else:
            print("Invalid option. Choose 0-6.")


if __name__ == "__main__":
    campus_management_simulation()
