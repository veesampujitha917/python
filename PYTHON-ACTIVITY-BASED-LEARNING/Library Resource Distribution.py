
def library_resource_distribution():
    inventory = {
        "Python": 30,
        "Databases": 20,
        "Networking": 15
    }

    branches = [
        ("Central", 1, {"Python": 12, "Databases": 8, "Networking": 5}),
        ("North", 2, {"Python": 15, "Databases": 10, "Networking": 8}),
        ("South", 3, {"Python": 10, "Databases": 6, "Networking": 6}),
    ]

    remaining = inventory.copy()
    unmet = {title: 0 for title in inventory}

    for branch, priority, requests in sorted(branches, key=lambda x: x[1]):
        print(f"\n{branch} Branch (Priority {priority})")

        for title, demand in requests.items():
            allocated = min(demand, remaining[title])
            remaining[title] -= allocated
            unmet[title] += demand - allocated

            print(
                f"{title}: Requested {demand}, "
                f"Allocated {allocated}, Unmet {demand - allocated}"
            )

    print("\nRemaining inventory:", remaining)
    print("Unmet demand:", unmet)


if __name__ == "__main__":
    library_resource_distribution()
