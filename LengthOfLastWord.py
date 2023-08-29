def lengthOfLastWord(s):
    l = list(s)
    count = 0
    index = 0
    l.reverse()

    if l[0] == " ":
        for i in range(1, len(l)):
            if l[i] != " ":
                index = i
                break

    for i in range(index, len(l)):
        if l[i] != " ":
            count += 1
        else:
            break
    return count

s = "luffy is still joyboy     "
print(lengthOfLastWord(s))