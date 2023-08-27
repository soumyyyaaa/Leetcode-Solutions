def findTheDifference(s, t):
    # s = list(s)
    # t = list(t)
    # for i in range(0, len(s)):
    #     for j in range(0, len(t)):
    #         if s[i] == t[j]:
    #             s[i] = " "
    #             t[j] = " "
    #             break
    # for letter in t:
    #     if letter != " ":
    #         return letter
    s=list(s)
    s.sort()
    t=list(t)
    t.sort()
    for i in range(len(s)):
        if t[i]!=s[i]:
            return t[i]            
    return t[-1]
    
s = "abcda"
t = "abecda"
print(findTheDifference(s, t))

