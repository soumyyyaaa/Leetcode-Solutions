def findNumbers(nums):
    even_digit = 0
    for i in range(0, len(nums)):
        list_num = str(nums[i])
        if len(list(list_num)) % 2 == 0:
            even_digit += 1
       
    return even_digit

nums = [12,345,2,6,7896]
print(findNumbers(nums))
        