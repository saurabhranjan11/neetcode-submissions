class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for num in nums:
            res[num] = res.get(num,0) + 1
        for num in res:
            if res[num] == 1:
                return num