class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        n = len(s)
        max_l = 0
        max_s = ""
        for i in range(n):
            # Odd
            l = self.palLen(s, i, i, n)
            # print("odd", i, i, l)
            if max_l < 2*l-1:
                max_l = 2*l-1
                max_s = s[i-l+1:i+l]

            # Even
            l = self.palLen(s, i, i+1, n)
            # print("even", i, i+1, l)
            if max_l < 2*l:
                max_l = 2*l
                max_s = s[i-l+1:i+l+1]
            # print("max", max_l, max_s)

        return max_s

    def palLen(self, s: str, i: int, j: int, n: int) -> int:
        l = 0
        while i >= 0 and j < n:
            if s[i] != s[j]:
                break
            l += 1
            i -= 1
            j += 1

        return l