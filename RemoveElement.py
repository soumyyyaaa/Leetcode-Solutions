def removeElement(nums, val):
    empty = []
    count = 0
    count_val = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            empty.append(nums[i])
            count_val += 1
        else: 
            count += 1
    for i in range(0, count):
        empty.append(0)
    nums = empty
    
    return count_val, nums

nums = [3,2,2,3]
val = 3
print(removeElement(nums,val))