def findMaxConsecutiveOnes(nums):
    count = 0
    count_arr = []
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count_arr.append(count)
            count = 0
        if i == len(nums) - 1:
            count_arr.append(count)
    return max(count_arr)

num = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(num))
