class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        cnt = 0
        max_cnt = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[cnt])
                cnt += 1
            seen.add(s[i])
            max_cnt = max(max_cnt, i - cnt + 1 )
        return max_cnt
