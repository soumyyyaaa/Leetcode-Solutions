def lengthOfLastWord(s):
    count = 0
    s = "".join(reversed(s.strip()))
    for char in s:
        if char != " ":
            count += 1
        else: 
            break
    
    return count

s = "luffy is still joyboy     "
print(lengthOfLastWord(s))