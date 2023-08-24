def sortedSquares(nums):
    square = []
    for ele in nums:
        square.append(ele * ele)
    square.sort()
    return square

nums = [-4,-1,0,3,10]
print(sortedSquares(nums))