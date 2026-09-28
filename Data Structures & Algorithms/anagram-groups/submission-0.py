class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for word in strs:
            new = "".join(sorted(word))
            if new not in mp:
                mp[new] = []
            mp[new].append(word)

        return list(mp.values())
