class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        n  = len(nums)
        new = []
        cnt = 1
        for i in range(1,n): 
            if nums[i-1] == nums[i]:
                cnt += 1
            else:
                new.append((cnt,nums[i-1]))
                cnt = 1
                
        if n > 0:
            new.append((cnt,nums[-1]))
        new.sort(reverse = True)
        freq = []
        for i in range(k):
            freq.append(new[i][1])
        return freq
        