def isAnagram(s, t):
    # s = list(s)
    # t = list(t)
    s.sort()
    t.sort()
    for letter in s:
        for character in t:
            if letter != character:
                return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))