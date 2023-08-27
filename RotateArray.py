def rotate(nums, k):
    # for i in range(0, k):
    #     temp = nums[len(nums) - 1]
    #     for j in range(len(nums) - 1, -1, -1):
    #         nums[j] = nums[j-1]
    #     nums[0] = temp
    last_arr = []
    for i in range(0, k):
        last_arr.append(nums.pop())
    last_arr.reverse()
    return last_arr

    
nums = [-1,-100,3,99]
k = 2
print(rotate(nums, k))
print(nums)