password = input("Enter password: ")

has_upper = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    if char in "@#$":
        has_special = True

if 8 <= len(password) <= 16 and has_upper and has_special:
    print("Password is Secure.")
else:
    print("Password is Not Secure.")
