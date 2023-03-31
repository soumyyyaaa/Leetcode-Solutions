def longestPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    else:
        commonLetters = ""
        smallestWordList = []
        isCommon = False
        minLen = len(strs[0])
        indexOfMinLenWord = 0
        for i in range(1, len(strs)):
            if len(strs[i]) <= minLen:
                minLen = len(strs[i])
                indexOfMinLenWord = i
        smallestWordList[:0] = strs[indexOfMinLenWord]
        for i in range(0, len(smallestWordList)):
            for j in range(0, len(strs)):
                if j == indexOfMinLenWord:
                    continue
                else:
                    if smallestWordList[i] == strs[j][i]:
                        isCommon = True
                    else:
                        isCommon = False
                        break
            if isCommon:
                commonLetters = commonLetters + smallestWordList[i]
            else:
                break
        return commonLetters

strs = ["cir","car"]
print(longestPrefix(strs))