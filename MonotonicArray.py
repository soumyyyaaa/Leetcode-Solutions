def isMonotonic(nums):
    increasing = 0
    decreasing = 0
    for i in range(0, len(nums) - 1):
        if nums[i] < nums[i+1]:
            increasing += 1
        elif nums[i] > nums[i+1]:
            decreasing += 1
        else:
            increasing += 1
            decreasing += 1
    if increasing == len(nums) - 1 or decreasing == len(nums) - 1:
        return True
    else:
        return False
    
nums = [1,3,2]
print(isMonotonic(nums))