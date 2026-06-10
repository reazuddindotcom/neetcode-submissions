class Solution:
    # V0: Without DP
    def __init__(self):
        self.count = {}
    def numDistinct(self, s: str, t: str) -> int:
        return self.dfs(s,t,0,0)
        
    def dfs(self, s: str, t: str, i: int, j: int) -> int:
        if j >= len(t):
            return 1
        elif i >= len(s):
            return 0
        if (i,j) in self.count:
            return self.count[(i,j)]

        # print(i,j)
        match = 0
        if j < len(t) and s[i] == t[j]:
            match = self.dfs(s, t, i+1, j+1)

        skip = self.dfs(s,t,i+1, j)
        
        self.count[(i,j)] = match+skip
        return self.count[(i,j)]


# TLE Input
# s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# t="aaaaaaaaaaaaaaaa"