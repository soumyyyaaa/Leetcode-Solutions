def generate(numRows):
    ans = [1,1]
    for i in range(2, numRows):
        if i == numRows-1:
            ans.append(1)
        else:
            ans.append(ans[i-1] + ans[i-2])
    return ans

print(generate(5))
        
            