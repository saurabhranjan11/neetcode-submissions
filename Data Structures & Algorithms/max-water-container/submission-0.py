class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = []
        for i in range(n):
            for j in range(n):
                l = min(heights[i], heights[j])
                b = j-i
                res.append(l*b)
        return max(res)
