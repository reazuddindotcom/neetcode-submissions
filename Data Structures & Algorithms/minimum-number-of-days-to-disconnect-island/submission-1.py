# If no 1: return 0
# If multiple: return 0
# If one: return 1 or 2
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])
        # print("R", R, "C", C)
        
        island = False
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    island = True
                    break
    
        if not island or not self.count_1(grid,R,C):
            return 0

        for r in range(R):
            for c in range(C):
                # print("grid",grid[r][c],r,c)
                if grid[r][c]:
                    grid[r][c] = 0
                    # print("zeroing",r,c)
                    if not self.count_1(grid,R,C):
                        return 1
                    grid[r][c] = 1
                    # print("no return")
                
        return 2

    def count_1(self, grid: List[List[int]], R: int, C: int):
        # True if 1 island
        # False if 2+ island
        # Copy the grid
        n_grid = [row[:] for row in grid]
        count = 0
        for r in range(R):
            for c in range(C):
                if n_grid[r][c]:
                    self.dfs(n_grid, R, C, r, c)
                    count += 1
                    if count > 1:
                        return False

        return False if count == 0 else True


    def dfs(self, grid: List[List[int]], R: int, C: int, r: int, c: int):
        grid[r][c] = 0
        for rr, cc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
            if rr >= 0 and rr < R and cc >= 0 and cc < C and grid[rr][cc]:
                self.dfs(grid,R,C,rr,cc)
        
# [[1,1,1],[1,1,1]]
# [[1,1,1]]
# [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
# [[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# [[1]]
# [[0,1,1,0],[0,0,0,0],[0,1,1,0]]
