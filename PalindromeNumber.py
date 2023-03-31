class Solution(object):
    def isPalindrome(self, x):
        b = str(x)
        for i in range(0,len(b),1):
            if b[i] == b[len(b)-i-1]:
                d=True
            else:
                d=False
                break
        return d