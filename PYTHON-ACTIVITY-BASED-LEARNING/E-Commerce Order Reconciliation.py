
def ecommerce_reconciliation():
    inventory = {
        "Keyboard": 20,
        "Mouse": 30,
        "Headphones": 15
    }

    prices = {
        "Keyboard": 800,
        "Mouse": 400,
        "Headphones": 1500
    }

    orders = [
        ("O101", "Keyboard", 3, 10, 3, 0),
        ("O102", "Mouse", 5, 5, 5, 1),
        ("O103", "Headphones", 2, 15, 2, 0),
        ("O104", "Keyboard", 2, 0, 1, 0),
        ("O105", "Mouse", 4, 10, 4, 0),
    ]

    gross_revenue = 0
    refunds = 0

    for order_id, product, qty, discount, dispatched, returned in orders:
        if qty > inventory[product]:
            print(f"{order_id}: Rejected - insufficient stock")
            continue

        inventory[product] -= dispatched

        unit_price = prices[product] * (1 - discount / 100)
        order_value = unit_price * dispatched
        refund = unit_price * returned
        net = order_value - refund

        gross_revenue += order_value
        refunds += refund

        print(f"\nOrder: {order_id} | Product: {product}")
        print(f"Ordered: {qty}, Dispatched: {dispatched}, Returned: {returned}")
        print(f"Dispatch value: ₹{order_value:.2f}")
        print(f"Refund: ₹{refund:.2f}")
        print(f"Net revenue: ₹{net:.2f}")

        if qty == dispatched:
            print("Dispatch status: MATCH")
        else:
            print(f"Dispatch discrepancy: {qty - dispatched} unit(s)")

    print("\nGross revenue:", f"₹{gross_revenue:.2f}")
    print("Refunds:", f"₹{refunds:.2f}")
    print("Net revenue:", f"₹{gross_revenue - refunds:.2f}")
    print("Remaining inventory:", inventory)


if __name__ == "__main__":
    ecommerce_reconciliation()
