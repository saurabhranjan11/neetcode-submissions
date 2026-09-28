class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        seen = set()
        res = []
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        triplet = (nums[i], nums[j] , nums[k])
                        if triplet in seen:
                            continue
                        res.append([nums[i], nums[j] ,nums[k]])
                        seen.add(triplet)
        return res