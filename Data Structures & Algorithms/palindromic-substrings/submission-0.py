class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        count = 0
        for i in range(n):
            # Odd
            count += self.palLen(s, i, i, n)

            # Even
            count += self.palLen(s, i, i+1, n)

        return count

    def palLen(self, s: str, i: int, j: int, n: int) -> int:
        l = 0
        while i >= 0 and j < n:
            if s[i] != s[j]:
                break
            l += 1
            i -= 1
            j += 1

        return l