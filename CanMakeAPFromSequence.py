def canMakeArithmeticProgression(arr):
    arr.sort()
    difference = arr[1] - arr[0]
    for i in range(0, len(arr) - 1):
        if (arr[i+1] - arr[i]) == difference:
            continue
        else:
            return False
    
    return True

arr = [3,5,1]
print(canMakeArithmeticProgression(arr))
    