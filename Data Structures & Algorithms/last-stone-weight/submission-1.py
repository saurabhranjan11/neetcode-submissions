class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = 0
        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if y != x:
                stones.append(x-y)
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]    