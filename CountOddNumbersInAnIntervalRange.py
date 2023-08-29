def countOdds(low, high):
    if low % 2 ==0 and high % 2 == 0:
        return int((high - low)/2)
    else:
        return int((high-low)/2 + 1)

low = 8
high = 10
print(countOdds(low, high))
