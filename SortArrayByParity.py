def sortArrayByParity(nums):
    odd_arr = []
    final_arr = []
    for i in range(0, len(nums)):
        if nums[i] % 2 != 0:
            odd_arr.append(nums[i])
        else:
            final_arr.append(nums[i])
    
    for ele in odd_arr:
        final_arr.append(ele)

    return final_arr

nums = [0,2,4,6,8,10]
print(sortArrayByParity(nums))