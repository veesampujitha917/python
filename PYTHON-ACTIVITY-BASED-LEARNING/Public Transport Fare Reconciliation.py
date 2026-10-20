
def transport_fare_reconciliation():
    fares = {
        "adult": 30,
        "student": 15,
        "senior": 20,
        "child": 10
    }

    trips = [
        ("Route A", "adult", 20, 600),
        ("Route A", "student", 10, 150),
        ("Route B", "senior", 8, 150),
        ("Route B", "child", 12, 120),
        ("Route C", "adult", 15, 420),
    ]

    total_expected = 0
    total_collected = 0

    for route, category, count, collected in trips:
        expected = fares[category] * count
        difference = collected - expected

        total_expected += expected
        total_collected += collected

        print(f"\n{route} | {category} x {count}")
        print("Expected:", expected)
        print("Collected:", collected)
        print("Difference:", difference)

        if difference < 0:
            print("Short collection")
        elif difference > 0:
            print("Excess collection")
        else:
            print("Reconciled")

    print("\nTotal expected:", total_expected)
    print("Total collected:", total_collected)
    print("Overall difference:", total_collected - total_expected)


if __name__ == "__main__":
    transport_fare_reconciliation()
