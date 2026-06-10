class Solution:
    # V0: Without DP --> Got TLE As expected
    # Although my initial non-DP approach got accepted – 
    # its not suitable to convert it to DP. Its hard to define a state.
    # To be able to define a state – we need to take one-character-step at a time.
    # V1: Without DP but more granular -- suitable for DP
    # V2: Trying with DP --> Got accepted with DP
    def __init__(self):
        self.is_il = {}
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        return self.dfs(s1,s2,s3,0,0,0)


    def dfs(self, s1: str, s2: str, s3: str, i: int, j: int, k: int) -> bool:
        # print(s1, s2, s3, i, j, k)
        if k >= len(s3):
            if i >= len(s1) and j >= len(s2):
                return True
            else:
                return False

        if (i,j) in self.is_il:
            return False

        if i < len(s1) and s1[i] == s3[k] and self.dfs(s1,s2,s3,i+1,j,k+1):
            # self.is_il[(i, j)] = True
            return True
        if j < len(s2) and s2[j] == s3[k] and self.dfs(s1,s2,s3,i,j+1,k+1):
            # self.is_il[(i, j)] = True
            return True

        self.is_il[(i, j)] = False
        return False

# I tried --
# s1="aaaa"
# s2="bbbb"
# s3="bbaabbaa"

# TLE Input
# s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

# Out of Index
# s1="aabcc"
# s2="dbbca"
# s3="aadbbcbcac"