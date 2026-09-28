class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new = set()
        for num in nums:
            if num in new:
                return num
            else:
                new.add(num)
        return None