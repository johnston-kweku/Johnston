sentence = input("Enter a sentece")
vowels = 0
consonants = 0

for char in sentence:
    if char .isalpha():
        if char .lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else :
            consonants += 1

print("Number of vowels: ", vowels)
print("Number of consonants: ", consonants)