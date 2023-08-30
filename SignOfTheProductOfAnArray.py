def arraySign(nums):
    # product = 1
    # for number in nums:
    #     product *= number
    # if product > 0:
    #     return 1
    # elif product < 0:
    #     return -1
    # elif product == 0:
    #     return 0
    count = 0
    for i in nums:
        if i == 0:
            return 0
        elif i < 0:
            count += 1
    if count % 2 == 0:
        return 1
    else:
        return -1

nums = [-1,1,-1,1,-1]
print(arraySign(nums))