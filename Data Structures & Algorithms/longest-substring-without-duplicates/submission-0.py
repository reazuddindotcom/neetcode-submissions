class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {}
        seen[s[0]] = 0
        l, r = 0, 0
        max_len = 1

        while r+1 < len(s):
            r += 1
            if s[r] not in seen or seen[s[r]] < l:
                seen[s[r]] = r
            else:
                max_len = max(max_len, r - l)
                l = seen[s[r]] + 1
                seen[s[r]] = r

        return max(max_len, r - l + 1)