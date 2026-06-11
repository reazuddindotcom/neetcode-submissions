class Solution:
    # V0: Without DP --> WA First. Lotta edge cases.
    # V1: Without DP, after looking at the coding video --> Got TLE
    def __init__(self):
        self.matches = {}
    def isMatch(self, s: str, p: str) -> bool:
        # Q: * cannot be at the beginning, right?
        # Q: What does 'matches' mean? Substring? E2E?
        return self.match(s,p,0,0)

    def match(self, s: str, p: str, i:int, j:int) -> bool:
        if i == len(s) and j == len(p):
            return True
        if j == len(p):
            return False

        if (i,j) in self.matches:
            return False

        cur_match =  i < len(s) and (p[j] == '.' or p[j] == s[i])
        if j+1 < len(p) and p[j+1] == '*':
            if self.match(s,p,i,j+2):
                return True

            if cur_match and self.match(s,p,i+1,j):
                return True

            self.matches[(i,j)] = False
            return False
        elif cur_match:
            if self.match(s,p,i+1,j+1):
                return True
            else:
                self.matches[(i,j)] = False
                return False
        else:
            self.matches[(i,j)] = False
            return False

# WA Before TLE
# s="aab"
# p="c*a*b"

# WA 2
# s="mississippi"
# p="mis*is*p*."

# WA 3
# s="a"
# p="ab*"


# TLE Input
# s="aaaaaaaaaaaaaaaaaaaa"
# p="a*a*a*a*a*a*a*a*a*a"