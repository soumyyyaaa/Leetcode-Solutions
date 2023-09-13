def repeatedSubstringPattern(s):
    copy = list(s)
    for char in s:
        copy.append(char)
    copy.pop()
    copy[0] = " "
    copy = ''.join(map(str, copy))
    if s in copy:
        return True
    else:
        return False

s = "abcabcabcabc"
print(repeatedSubstringPattern(s))