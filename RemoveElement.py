def removeElement(nums, val):
    removed_val_count = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            removed_val_count += 1
            for j in range(i, len(nums) - 1):
                nums[j] = nums[j+1]
            nums.pop()
            nums.append(-1)
            i -= 1
        else:
            i += 1

    return  len(nums)-removed_val_count,nums

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums,val))