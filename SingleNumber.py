def singleNumber(nums):
    nums.sort()
    for i in range(0, len(nums), 2):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                break
            else:
                return nums[i]
    return nums[i]

nums = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
print(singleNumber(nums))
