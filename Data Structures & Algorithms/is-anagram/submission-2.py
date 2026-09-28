class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        
        res = {}
        for ch in s:
            res[ch] = res.get(ch,0) + 1
        
        for ch in t:
            if ch not in res:
                return False
                
            res[ch] -= 1
            if res[ch] == 0:
                del res[ch]
        return len(res) == 0
