class Solution(object):
    def countOdds(self, low, high):
        odd = 0
        if low % 2 ==0 and high % 2 == 0:
            return (high - low)/2
        else:
            return (high-low)/2 + 1

