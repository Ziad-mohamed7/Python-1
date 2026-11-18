number = int(input("Enter a number: "))

while number >= 10:
    total = 0

    for digit in str(number):
        total += int(digit)

    number = total

print("Digital Root:", number)
