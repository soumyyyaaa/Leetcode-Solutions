def duplicateZeros(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            for j in range(len(arr)-1, i, -1):
                arr[j] = arr[j-1]
            arr[i+1] = 0
            i += 2
        else:
            i += 1
    return arr

arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(arr))