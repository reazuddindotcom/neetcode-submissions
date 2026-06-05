class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid,r,c,R,C)

        return count
    
    def bfs(self, grid: List[List[str]], r: int, c: int, R: int, C: int) -> None:
        queue = deque()
        queue.append((r,c))

        while queue:
            r, c = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == "0":
                continue

            grid[r][c] = "0" # visited (or flooded)

            queue.append((r+1, c))
            queue.append((r-1, c))
            queue.append((r, c+1))
            queue.append((r, c-1))
