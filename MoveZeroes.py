def moveZeroes(nums):
    # count = 0
    # i = 0
    # while i < len(nums):
    #     if nums[i] == 0:
    #         for j in range(i, len(nums) -1):
    #             nums[j] = nums[j+1]
    #         nums.pop()
    #         count += 1
    #         i -= 1
    #     i += 1
    # for k in range(0, count):
    #     nums.append(0)
    index = 0
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1

    while index < len(nums):
        nums[index] = 0
        index += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)