def reverseVowels(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    empty_vowel_array = []
    for letter in s:
        if letter in vowel:
            letter.append(empty_vowel_array)
    li = empty_vowel_array[::-1]
    return li

s = "hello"
print(reverseVowels(s))