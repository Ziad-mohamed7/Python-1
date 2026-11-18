store = {"apple": 0.5, "bread": 2.0, "milk": 1.5}

cart = []

while True:
    action = input("Enter Add, Remove, or Done: ").lower()

    if action == "done":
        break

    item = input("Enter item name: ").lower()

    if action == "add":
        if item in store:
            cart.append(item)
            print(item, "added.")
        else:
            print("Error: Item not found.")

    elif action == "remove":
        if item in cart:
            cart.remove(item)
            print(item, "removed.")
        else:
            print("Item not in cart.")

    else:
        print("Invalid action.")

total = 0

for item in cart:
    total += store[item]

print("Total Bill: $", round(total, 2))
