
def manufacturing_production_planner():
    products = {
        "Chair": {
            "demand": 100, "stock": 30,
            "material_per_unit": 2, "planned": 80, "defects": 4
        },
        "Table": {
            "demand": 50, "stock": 10,
            "material_per_unit": 5, "planned": 45, "defects": 6
        },
        "Shelf": {
            "demand": 70, "stock": 20,
            "material_per_unit": 3, "planned": 60, "defects": 2
        },
    }

    raw_material = 600
    defect_limit = 5
    total_material = 0

    for name, data in products.items():
        material = data["planned"] * data["material_per_unit"]
        total_material += material

        good_units = data["planned"] - data["defects"]
        available = data["stock"] + good_units
        shortage = max(0, data["demand"] - available)
        defect_rate = data["defects"] / data["planned"] * 100

        print(f"\nProduct: {name}")
        print("Material required:", material)
        print("Good units produced:", good_units)
        print("Total available:", available)
        print("Demand shortage:", shortage)
        print(f"Defect rate: {defect_rate:.2f}%")
        print("Quality:", "VIOLATION" if defect_rate > defect_limit else "OK")

    print("\nTotal material required:", total_material)
    if total_material <= raw_material:
        print("Material feasibility: FEASIBLE")
    else:
        print("Material shortage:", total_material - raw_material)


if __name__ == "__main__":
    manufacturing_production_planner()
