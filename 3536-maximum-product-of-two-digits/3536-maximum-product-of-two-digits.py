class Solution(object):
    def maxProduct(self, n):
        n=sorted(int(i) for i in str(n))
        return n[-1]*n[-2]