def removeDuplicates(nums):
    emptyList = []
    for i in range(0, len(nums) - 1):
        if nums[i] != nums[i+1]:
            emptyList.append(nums[i])
    emptyList.append(nums[len(nums) - 1])
    lengthOfUniqueInt = len(emptyList)
    for i in range(lengthOfUniqueInt, len(nums)):
        emptyList.append("_")
    return lengthOfUniqueInt, emptyList

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))