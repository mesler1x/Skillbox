string = input()

vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщ'

vowel_sum = 0
consonant_sum = 0

for char in string:
    if char.lower() in vowels:
        vowel_sum += 1
    elif char.lower() in consonants:
        consonant_sum += 1

print(vowel_sum, consonant_sum)
