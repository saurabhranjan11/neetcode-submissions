class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        res = []
        for i in range(n):
            new = 1
            for j in range(n):
                if i == j:
                    continue

                new *= nums[j]
            res.append(new)
        return res

        