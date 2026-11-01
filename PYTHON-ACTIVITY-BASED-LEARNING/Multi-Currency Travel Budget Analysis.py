rupees = float(input("Enter budget in INR: "))
rate = float(input("Enter exchange rate (1 foreign unit in INR): "))

foreign_money = rupees / rate

print("Budget in foreign currency =", round(foreign_money, 2))