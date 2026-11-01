amount = float(input("Enter total purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = amount * 0.05

final_bill = amount - discount

print("Discount =", discount)
print("Final Bill =", final_bill)