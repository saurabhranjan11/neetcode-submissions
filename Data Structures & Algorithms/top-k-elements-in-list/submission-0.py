class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = {}
        for x in nums:
            new[x] = new.get(x,0) + 1
        new = dict(sorted(new.items(),key = lambda x:x[1], reverse = True))
        cnt = 0
        res = []
        for key,val in new.items():
            if cnt == k:
                break
            res.append(key)
            cnt += 1
        return res