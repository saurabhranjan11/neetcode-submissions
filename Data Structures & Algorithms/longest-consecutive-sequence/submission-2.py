class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr = 1
        nums.sort()
        longest = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                continue
            elif nums[i-1] + 1 == nums[i]:
                curr += 1
                longest = max(longest,curr)
            else:
                curr = 1
        return longest