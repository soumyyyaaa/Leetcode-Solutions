def mergeAlternately(word1, word2):
    merged = ""
    word1 = list(map(str, word1))
    word2 = list(map(str, word2))
    if len(word1) > len(word2):
        for i in range((len(word1) - len(word2)), 0, -1):
            merged += word1.pop()
    elif len(word2) > len(word1):
        for i in range((len(word2) - len(word1)), 0, -1):
            merged += word2.pop()
    for i in range(0, (len(word1) + len(word2))):
        if i % 2 == 0:  
            merged += word2.pop()
        else:
            merged += word1.pop()
    merged = "".join(reversed(merged))
    return merged

word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))