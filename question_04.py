list1 = input("Enter first list of names: ").split(",")
list2 = input("Enter second list of names: ").split(",")

list1 = [name.strip() for name in list1]
list2 = [name.strip() for name in list2]

common = []

for name in list1:
    if name in list2 and name not in common:
        common.append(name)

print("Common names:", common)
