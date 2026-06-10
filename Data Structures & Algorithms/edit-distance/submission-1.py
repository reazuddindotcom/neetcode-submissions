class Solution:
    # V0: Without DP --> Got TLE as expected.
    # V1: With DP
    def __init__(self):
        self.dist = {}
    def minDistance(self, word1: str, word2: str) -> int:
        # if not word1:
        #     return len(word2)
        # if not word2:
        #     return len(word1)

        return self.dfs(word1, word2, 0, 0)

    def dfs(self, w1: str, w2: str, i: int, j: int) -> int:
        if i == len(w1):
            return len(w2) - j

        if j == len(w2):
            return len(w1) - i

        if (i,j) in self.dist:
            return self.dist[(i,j)]

        dist = 0
        if w1[i] == w2[j]:
            dist = self.dfs(w1, w2, i+1, j+1)
        else:
            delete = self.dfs(w1, w2, i+1, j) + 1
            insert = self.dfs(w1, w2, i, j+1) + 1
            replace = self.dfs(w1, w2, i+1, j+1) + 1
            dist = min(delete, insert, replace)

        self.dist[(i,j)] = dist
        return self.dist[(i,j)]
        
# TLE Example
# "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghij"
# "jihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcbajihgfedcba"