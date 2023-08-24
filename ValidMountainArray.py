def validMountainArray(arr):
    if len(arr) < 3:
        return False
    else:
        maximum_element_index = arr.index(max(arr))
        if maximum_element_index == 0 or maximum_element_index == len(arr)-1:
            return False
        for i in range(0, maximum_element_index):
            if arr[i] >= arr[i+1]:
                return False
        for j in range(maximum_element_index, len(arr) - 1):
            if arr[j] <= arr[j+1]:
                return False
        return True

arr = [0,1,2,4,2,1]
print(validMountainArray(arr))