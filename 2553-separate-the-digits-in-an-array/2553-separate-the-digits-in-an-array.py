class Solution(object):
    def separateDigits(self, nums):
        n=""
        for i in nums:
            for j in str(i):
                n+=j
        return[int(i) for i in n]