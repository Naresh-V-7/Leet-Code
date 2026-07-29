class Solution(object):
    def sumAndMultiply(self, num):
        if num==0:return 0
        n=""
        for i in str(num):
            if i!="0":n+=i
        n=int(n)
        temp=n
        c=0
        while(n>0):
            c+=n%10
            n//=10
        return temp*c