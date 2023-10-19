def create_palindrome(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    middle_char = ''
    palindrome = ''

    for char in char_count:
        if char_count[char] % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return "Невозможно сформировать палиндром из данного слова."
            else:
                middle_char = char

        for _ in range(char_count[char] // 2):
            palindrome += char

    return palindrome + middle_char + palindrome[::-1]

