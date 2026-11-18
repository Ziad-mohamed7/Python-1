word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if len(word1) == len(word2):
    result = ""

    for i in range(len(word1)):
        result += word1[i] + word2[i]

    print(result)
else:
    print("Words must have the same length.")
