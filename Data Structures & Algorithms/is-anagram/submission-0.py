class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if n != m:
            return False
        k = list(s)
        l = list(t)
        k.sort()
        l.sort()

        for i in range(n):
            if k[i] != l[i]:
                return False
        return True
            