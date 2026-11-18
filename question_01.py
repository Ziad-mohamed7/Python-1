text = input("Enter a string: ")

letters = []
numbers = []

for char in text:
    if char.isalpha():
        letters.append(char)

    elif char.isdigit():
        numbers.append(int(char))

word = "".join(letters)
total = sum(numbers)

print("Word:", word)
print("Sum:", total)
