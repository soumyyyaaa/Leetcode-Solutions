def roman(s):
    romanNum = []
    romanNum[:0] = s
    numeric = []
    for i in range(0, len(romanNum)):
        if romanNum[i] == "I":
            numeric.append(1)
        elif romanNum[i] == "V":
            numeric.append(5)
        elif romanNum[i] == "X":
            numeric.append(10)
        elif romanNum[i] == "L":
            numeric.append(50)
        elif romanNum[i] == "C":
            numeric.append(100)
        elif romanNum[i] == "D":
            numeric.append(500)
        elif romanNum[i] == "M":
            numeric.append(1000)

    convertedNum = 0
    for i in range(0, len(romanNum) - 1):
        if numeric[i] >= numeric[i+1]:
            convertedNum = convertedNum + numeric[i]
        else:
            convertedNum = convertedNum - numeric[i]
    
    convertedNum = convertedNum + numeric[-1]
    return convertedNum

s= "MMMCDXC"
print(roman(s))
