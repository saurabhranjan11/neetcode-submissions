class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = []
        if n<2:
            return 0
        for i in range(n):
            for j in range(i+1, n):
                if prices[i] >= prices[j]:
                    continue
                profit.append(prices[j] - prices[i])
        if len(profit) == 0:
            return 0
        res = max(profit)
        if res <= 0:
            return 0
        return res
