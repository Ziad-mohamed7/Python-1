data = {"A": 1, "B": 2, "C": 1}

reversed_dict = {}

for key, value in data.items():
    if value not in reversed_dict:
        reversed_dict[value] = []

    reversed_dict[value].append(key)

print(reversed_dict)
