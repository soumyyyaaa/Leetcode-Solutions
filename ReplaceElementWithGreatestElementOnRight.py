def replaceElements(arr):
    i = 0
    condition = True
    empty_arr = []
    while condition:
        max_ele = max(arr)
        max_ele_ind = arr.index(max_ele)

        while i < max_ele_ind:
            empty_arr.append(max_ele)
            arr[i] = -1
            i += 1
        
        arr[max_ele_ind] = -1

        if max_ele_ind == len(arr) - 1:
            condition = False

        i = max_ele_ind
    empty_arr.append(-1)
    
    return empty_arr

arr = [400]
print(replaceElements(arr))