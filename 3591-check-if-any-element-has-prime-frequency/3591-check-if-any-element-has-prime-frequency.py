class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        n=Counter(nums)
        for i in n:
            if n[i]>1:    
                c=0
                for j in range(2,n[i]//2+1):
                    if n[i]%j==0:c=1
                if c==0:return True
        else:return False
            