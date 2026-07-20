class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        if not wordDict:
            return False

        s_len = len(s)
        possible = [False]*(s_len+1)
        possible[0] = True # before start of s

        for i in range(1, s_len+1, 1):
            for w in wordDict:
                l = len(w)
                if i - l >= 0 and possible[i-l] and s[i-l:i] == w:
                    possible[i] = True
                    break

        return possible[s_len]
