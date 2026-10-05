class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        new = {}
        for i in range(len(s)):
            new[s[i]] = new.get(s[i], 0) + 1
        for i in range(len(t)):
            if t[i] not in new:
                return False
            new[t[i]] -= 1
        if all(value == 0 for value in new.values()):
            return True
        return False