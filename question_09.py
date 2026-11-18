n = int(input("Enter a number: "))

factorial = 1
total = 0

for i in range(1, n + 1):
    factorial *= i
    total += i

print("Factorial is", factorial)
print("Sum is", total)

if total != 0 and factorial % total == 0:
    print(f"{factorial} is divisible by {total}.")
else:
    print(f"{factorial} is not divisible by {total}.")
