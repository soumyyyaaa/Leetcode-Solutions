def isValid(s):
    convertString = []
    convertString[:0] = s

    for i in range(0, len(convertString)):
        if convertString[i] == "[":
            for j in range(0, len(convertString)):
                if convertString[j] == "]":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
        elif convertString[i] == "]":
            for j in range(0, len(convertString)):
                if convertString[j] == "[":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
        elif convertString[i] == "(":
            for j in range(0, len(convertString)):
                if convertString[j] == ")":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
        elif convertString[i] == ")":
            for j in range(0, len(convertString)):
                if convertString[j] == "(":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
        elif convertString[i] == "{":
            for j in range(0, len(convertString)):
                if convertString[j] == "}":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
        elif convertString[i] == "}":
            for j in range(0, len(convertString)):
                if convertString[j] == "{":
                    convertString[j] = 0
                    convertString[i] = 0
                    break
    
    count = 0
    for i in range(0, len(convertString)):
        if convertString[i] == 0:
            count = count + 1
    if count == len(convertString):
        return "true"
    else: 
        return "false"

s = "(]"
print(isValid(s))
