class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        if len(nums) < 2:
            return False
        
        for num in nums:
            res[num] = res.get(num,0) + 1
            if res[num] > 1:
                return True
        return False