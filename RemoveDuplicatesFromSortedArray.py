def removeDuplicates(nums):
    empty_arr = []
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            empty_arr.append(nums[i-1])
    empty_arr.append(nums[len(nums) - 1])
    for j in range(0, len(nums)):
        nums.pop()
    for k in range(0, len(empty_arr)):
        nums.append(empty_arr[k])

    return len(empty_arr)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))