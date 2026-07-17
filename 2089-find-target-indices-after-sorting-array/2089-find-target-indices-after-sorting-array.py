class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums=sorted(nums)
        j=[]
        for i in range(len(nums)):
            if nums[i]==target:
                j.append(i)
        return j

