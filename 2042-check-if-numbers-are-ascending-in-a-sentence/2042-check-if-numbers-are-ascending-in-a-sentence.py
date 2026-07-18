class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        s=[int(i) for i in s if i.isdigit() ]
        return s==sorted(set(s))