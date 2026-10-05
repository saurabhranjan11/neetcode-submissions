class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        new  = sorted(s)
        view = sorted(t)
        for i in range(len(s)):
            if new[i] != view[i]:
                return False
        return True