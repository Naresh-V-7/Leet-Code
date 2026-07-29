class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            if goal==(s[i+1:]+s[:i+1]):
                return True
        else: return False
        