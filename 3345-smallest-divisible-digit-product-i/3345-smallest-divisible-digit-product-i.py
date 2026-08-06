import itertools
class Solution(object):
    def smallestNumber(self, n, t):
        for i in itertools.count(n):
            r=i
            s=1
            while(r>0):
                s*=r%10
                r//=10
            if s%t==0:return i
