class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_s = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            map_s[sorted_s].append(s)

        return list(map_s.values())