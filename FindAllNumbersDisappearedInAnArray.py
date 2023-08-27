def findDisappearedNumbers(nums):
    ele = []
    arr = [False] * (len(nums) + 1)
    for i in range(1, len(nums) +1):
        for j in range(0, len(nums)):
            if i == nums[j]:
                arr[i] = True
                break
        if arr[i] != True:
            ele.append(i)
   
    return ele

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))