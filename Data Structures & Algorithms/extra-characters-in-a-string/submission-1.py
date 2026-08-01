class Solution:
    def __init__(self):
        self.dp = []
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Q any limit on # of extra characters? 
        # continue upto neet. 
        # V0 no DP

        self.dp = [float("inf")] * len(s)
        # print("length s ", len(s))
        # print("length dp ", len(self.dp))
        return self.dfs(s, 0, set(dictionary))

    def dfs(self, s: str, i: int, dictionary: set) -> int:
        if i == len(s):
            return 0

        # print("i ", i)
        if self.dp[i] != float("inf"):
            return self.dp[i]

        min_x = self.dfs(s, i+1, dictionary) + 1 # skipping current character
        for w in dictionary:
            # l = len(w) i+l <= len(s) and 
            if s.startswith(w, i):
                print("\t", w)
                min_x = min(min_x, self.dfs(s, i+len(w), dictionary))

        self.dp[i] = min_x
        return min_x

        
# V0 No DP TLE
# s="enknouowgowcipfipojlrpuowgoiogiiebfjiafwksaigjyd"
# dictionary=["gw","lq","yzqch","sah","giieb","kfqczw","qxqz","jb","ucxmpe","hpwr","y","vzlhe","i","kn","ip","iafwk","zl","dw","yhxeqi","egktb","xasq","f","c","vrllz","p","uowgo","pgxd","gnjgkm","rnug","sa","vfccq","j"]

