class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1).intersection(set(nums2)) !=set():
            return sorted(set(nums1).intersection(set(nums2)))[0]
        else:return -1