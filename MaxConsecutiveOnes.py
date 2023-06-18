def findMaxConsecutiveOnes(nums):
    arr = []
    for i in range(0, len(nums)):
        if nums[i] == 1:
            consecutive = 1
            for j in range(i+1, len(nums)):
                consecutive += 1
                if nums[j] != 1:
                    i = j
                    break
            arr.append(consecutive)
    """ maximum = arr[0]
    for i in range(1, len(arr)):
        if maximum < arr[i]:
            maximum = arr[i] """
    return arr                 
            

num = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(num))

