def romanToInt(s):
    # romanNum = []
    # romanNum[:0] = s
    # numeric = []
    # for i in range(0, len(romanNum)):
    #     if romanNum[i] == "I":
    #         numeric.append(1)
    #     elif romanNum[i] == "V":
    #         numeric.append(5)
    #     elif romanNum[i] == "X":
    #         numeric.append(10)
    #     elif romanNum[i] == "L":
    #         numeric.append(50)
    #     elif romanNum[i] == "C":
    #         numeric.append(100)
    #     elif romanNum[i] == "D":
    #         numeric.append(500)
    #     elif romanNum[i] == "M":
    #         numeric.append(1000)

    # convertedNum = 0
    # for i in range(0, len(romanNum) - 1):
    #     if numeric[i] >= numeric[i+1]:
    #         convertedNum = convertedNum + numeric[i]
    #     else:
    #         convertedNum = convertedNum - numeric[i]
    
    # convertedNum = convertedNum + numeric[-1]
    # return convertedNum
    s = list(s)
    conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    li_for_I = ["V", "X"]
    li_for_X = ["L", "C"]
    li_for_C = ["D", "M"]

    number = 0

    for i in range(0, len(s)):
        if s[i] in conversion:
            number += conversion[s[i]]
        if i!= 0:
            if s[i] in li_for_I:
                if s[i - 1] == "I":
                    number -= 2
            elif s[i] in li_for_X:
                if s[i - 1] == "X":
                    number -= 20
            elif s[i] in li_for_C:
                if s[i - 1] == "C":
                    number -= 200

    return number

s = "MCMXCIV"
print(romanToInt(s))
