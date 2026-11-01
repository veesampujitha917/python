
def find_student(students, sid):
    return next((s for s in students if s["id"] == sid), None)

students = [{"id":"ST101","name":"Asha","attendance":[],"marks":[],"events":[]},{"id":"ST102","name":"Ravi","attendance":[],"marks":[],"events":[]}]
resources={"Projectors":5,"Laptops":10,"Sports Kits":8}
events={"E1":"Tech Fest","E2":"Sports Day"}

while True:
    print("\nSMART CAMPUS MANAGEMENT\n1. List\n2. Attendance\n3. Marks\n4. Register event\n5. Resources\n6. Summary\n0. Exit")
    ch=input("Choose: ").strip()
    if ch=="0": break
    if ch=="1":
        for s in students: print(f"{s['id']} {s['name']} | {s['attendance']} | {s['marks']} | {s['events']}")
    elif ch=="2":
        sid=input("Student ID: ").strip().upper(); s=find_student(students,sid)
        if not s: print("Student not found."); continue
        status=input("P/A: ").strip().upper()
        if status in ("P","A"): s["attendance"].append(status); print("Attendance recorded.")
        else: print("Enter P or A.")
    elif ch=="3":
        sid=input("Student ID: ").strip().upper(); s=find_student(students,sid)
        if not s: print("Student not found."); continue
        subject=input("Subject: ").strip();
        try: mark=float(input("Mark: "))
        except ValueError: print("Enter a number."); continue
        if subject and 0<=mark<=100: s["marks"].append((subject,mark)); print("Mark saved.")
        else: print("Invalid mark.")
    elif ch=="4":
        sid=input("Student ID: ").strip().upper(); s=find_student(students,sid)
        if not s: print("Student not found."); continue
        eid=input("Event ID: ").strip().upper(); e=events.get(eid)
        if not e: print("Event not found.")
        elif eid in s["events"]: print("Already registered.")
        else: s["events"].append(eid); print(f"Registered for {e}")
    elif ch=="5":
        print("Resources:",resources)
        item=input("Resource: ").strip().title();
        if item not in resources: print("Unknown resource."); continue
        try: qty=int(input("Quantity: "))
        except ValueError: print("Enter a whole number."); continue
        if qty<=0 or qty>resources[item]: print("Invalid quantity.")
        else: resources[item]-=qty; print(f"Allocated {qty} {item}. Remaining: {resources[item]}")
    elif ch=="6":
        print("\nCAMPUS SUMMARY")
        for s in students:
            total=len(s["attendance"]); att=(s["attendance"].count("P")/total*100) if total else 0
            avg=(sum(m for _,m in s["marks"])/len(s["marks"])) if s["marks"] else 0
            print(f"{s['id']} - {s['name']}\nAttendance: {att:.1f}%\nAverage marks: {avg:.1f}\nEvents: {len(s['events'])}")
        print("Remaining resources:",resources)
    else: print("Invalid option.")
