text = input("Enter a string: ")

vowels = "aeiou"
result = {}

for i, char in enumerate(text.lower()):
    if char in vowels:
        if char not in result:
            result[char] = []

        result[char].append(i)

print(result)
