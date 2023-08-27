def heightChecker(heights):
    count = 0
    sorted_heights = sorted(heights)
    for i in range(0, len(heights)):
        if heights[i] != sorted_heights[i]:
                count += 1
    
    return count

heights = [1,2,3,4,5]
print(heightChecker(heights))