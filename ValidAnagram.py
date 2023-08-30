def isAnagram(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if len(s) != len(t):
        return False
    else:
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
    return True

s = "bat"
t = "tab"
print(isAnagram(s, t))