def kidsWithCandies(candies, extra_candy):
    max_candy = max(candies)
    output_array = []
    for candy in candies:
        if (candy + extra_candy) >= max_candy:
            output_array.append(True)
        else:
            output_array.append(False)
    return output_array

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))

