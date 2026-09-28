class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1,n+1):
            res[i] = self.solve(i)
        return res
    
    def solve(self, x: int) -> int:
        cnt = 0
        while x:
            cnt += x & 1
            x >>= 1
        return cnt
