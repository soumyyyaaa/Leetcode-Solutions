def largestPerimeter(nums):
    for i in range(0, len(nums) - 3, 3):
        extra = []
        for j in range (i, i+3):
            extra.append(nums[i])
        extra.sort()
        if (extra[0] + extra[1]) > extra[2]:
            return sum(extra)
    return 0

nums = [3,6,2,3]
print(largestPerimeter(nums))