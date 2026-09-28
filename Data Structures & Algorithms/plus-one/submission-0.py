class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = int("".join(map(str, digits)))
        total = new + 1
        res = list((map(int, str(total))))
        return res