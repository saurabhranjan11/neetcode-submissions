class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []
        for i in range(n):
            cnt = 0
            for j in range(i+1,n):
                cnt += 1
                if temperatures[j] > temperatures[i]:
                    break
                if (j == n-1):
                    cnt = 0


            res.append(cnt)

        return res