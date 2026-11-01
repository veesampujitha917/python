total = int(input("Enter total classes: "))
attended = int(input("Enter classes attended: "))

percentage = (attended / total) * 100

print("Attendance Percentage =", round(percentage, 2), "%")

if percentage >= 75:
    print("Attendance is sufficient")
else:
    required = (0.75 * total - attended) / 0.25
    print("More classes to attend =", max(0, int(required) + 1))