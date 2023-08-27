def thirdMax(nums):
    nums.sort()
    empty_arr = []
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            empty_arr.append(nums[i-1])
    empty_arr.append(nums[len(nums) - 1])
    for j in range(0, len(nums)):
        nums.pop()
    for k in range(0, len(empty_arr)):
        nums.append(empty_arr[k])
    if len(nums) < 3:
        return max(nums)
    else:
        third_max_ele = nums[nums.index(max(nums)) - 2]
        return third_max_ele

nums = [3,2,1]
print(thirdMax(nums))