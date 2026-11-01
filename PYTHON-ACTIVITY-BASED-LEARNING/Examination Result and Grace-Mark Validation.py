marks = int(input("Enter marks out of 100: "))

if marks >= 35:
    print("Result: Pass")
elif marks >= 30:
    grace = 35 - marks
    print("Grace Marks Required =", grace)
    print("Result: Eligible for grace marks (if permitted)")
else:
    print("Result: Fail")