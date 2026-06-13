class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])

        min_t = float("inf")
        max_t = 0
        for r in range(R):
            for c in range(C):
                min_t = min(min_t, grid[r][c])
                max_t = max(max_t, grid[r][c])

        mid = -1
        while min_t < max_t:
            mid = min_t + (max_t - min_t)//2
            if self.dfs(grid,0,0,set(),R,C,mid):
                max_t = mid
            else:
                min_t = mid+1

        return min_t

    def dfs(self, grid: List[List[int]], r:int, c:int, visited: Set, R: int, C: int, t: int) -> bool:
        if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] > t or (r,c) in visited:
            return False

        if r == R-1 and c == C-1:
            return True

        visited.add((r,c))
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        for i in range(4):
            rr = r+dr[i]
            cc = c+dc[i]
            if self.dfs(grid, rr, cc, visited, R, C, t):
                return True

        return False

# WA [[3,2],[0,1]] --> level of [0][0] needs to be checked as well