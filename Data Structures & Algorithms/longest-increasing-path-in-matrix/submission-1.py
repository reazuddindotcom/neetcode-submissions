class Solution:
    # V0: Without DP --> Got TLE as expected
    # V1: With DP
    def __init__(self):
        self.lip = {}
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix)
        if R == 0:
            return 0
        C = len(matrix[0])

        max_p = 0
        for r in range(R):
            for c in range(C):
                max_p = max(max_p, self.dfs(matrix,R,C,r,c))

        return max_p
        
    def dfs(self, matrix: List[List[int]], R: int, C: int, r: int, c: int) -> int:
        # Boundary check not needed as they are checked before the call
        # Visited not needed as its strictly increasing
        if (r,c) in self.lip:
            return self.lip[(r,c)]

        left, right, up, down = 1,1,1,1
        if r+1 < R and matrix[r][c] < matrix[r+1][c]:
            right = self.dfs(matrix, R, C, r+1, c) + 1
        if r-1 >=0 and matrix[r][c] < matrix[r-1][c]:
            left = self.dfs(matrix, R, C, r-1, c) + 1
        if c+1 < C and matrix[r][c] < matrix[r][c+1]:
            up = self.dfs(matrix, R, C, r, c+1) + 1
        if c-1 >= 0 and matrix[r][c] < matrix[r][c-1]:
            down = self.dfs(matrix, R, C, r, c-1) + 1

        self.lip[(r,c)] = max(left, right, up, down)
        return self.lip[(r,c)]

        
