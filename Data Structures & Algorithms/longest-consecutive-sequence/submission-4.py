class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
    
        for n in s:
            if n-1 not in s:
                new = n
                cnt = 1
                while new + 1 in s:
                    cnt += 1
                    new += 1
                longest = max(longest, cnt)
        return longest