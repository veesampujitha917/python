
def disaster_relief_allocation():
    stock = {
        "water": 100,
        "food": 80,
        "blankets": 40
    }

    areas = [
        ("Area North", 1, {"water": 50, "food": 35, "blankets": 20}),
        ("Area East", 2, {"water": 45, "food": 40, "blankets": 15}),
        ("Area South", 3, {"water": 30, "food": 25, "blankets": 20}),
    ]

    remaining = stock.copy()
    unmet_total = {item: 0 for item in stock}

    for area, priority, needs in sorted(areas, key=lambda x: x[1]):
        print(f"\n{area} (Priority {priority})")

        for item, need in needs.items():
            allocated = min(need, remaining[item])
            unmet = need - allocated

            remaining[item] -= allocated
            unmet_total[item] += unmet

            print(
                f"{item.title()}: Needed {need}, "
                f"Allocated {allocated}, Unmet {unmet}"
            )

    print("\nRemaining stock:", remaining)
    print("Total unmet demand:", unmet_total)


if __name__ == "__main__":
    disaster_relief_allocation()
