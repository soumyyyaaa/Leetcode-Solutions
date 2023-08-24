def checkIfExist(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] * 2 or arr[i] == arr[j] / 2:
                return True
    
    return False
            
arr = [3,1,7,11]
print(checkIfExist(arr))