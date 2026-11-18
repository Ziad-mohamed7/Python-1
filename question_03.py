price = float(input("Enter total price: "))
member = input("Are you a member? (Yes/No): ")

if price < 50:
    discount = 0
elif price <= 100:
    discount = 0.10
else:
    discount = 0.20

final_price = price - (price * discount)

if member.lower() == "yes":
    final_price = final_price * 0.95

print("Final Total: $", round(final_price, 2))
