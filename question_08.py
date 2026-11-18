numbers = [1, 1, 2, 3, 3, 3, 4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

result = []

for num, count in frequency.items():
    result.append((num, count))

print(result)
