class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_map = {}

        for i in range(len(s)):
            count_map[(s[i])] = count_map.get(s[i], 0) + 1
            count_map[(t[i])] = count_map.get(t[i], 0) - 1

        for i in count_map:
            if count_map[i] != 0:
                return False

        return True
        