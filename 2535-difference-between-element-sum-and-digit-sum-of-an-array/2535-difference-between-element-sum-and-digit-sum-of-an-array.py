class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            while(i>0):
                c+=i%10
                i//=10
        return abs(c-sum(nums))
            

        