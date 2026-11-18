sentence = input("Enter a sentence: ")

cleaned = sentence.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)
