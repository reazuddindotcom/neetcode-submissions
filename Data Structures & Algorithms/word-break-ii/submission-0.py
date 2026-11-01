class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        if len(s) == 1:
            return s

        result = []
        cur = []
        self.dfs(s, 0, set(wordDict), cur, result)

        return result

    def dfs(self, s: str, i: int, wordDict: set, cur: [], result: []) -> None:
        if i == len(s):
            result.append(" ".join(cur))
            return

        j = i + 1
        while j < len(s)+1:
            if s[i:j] in wordDict:
                cur.append(s[i:j])
                self.dfs(s, j, wordDict, cur, result)
                cur.pop()
            j += 1

        