class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    # self.bfs(grid,r,c,R,C)
                    self.bfs(grid,r+1,c,R,C)
                    self.bfs(grid,r-1,c,R,C)
                    self.bfs(grid,r,c+1,R,C)
                    self.bfs(grid,r,c-1,R,C)

    def bfs(self, grid: List[List[str]], r: int, c: int, R: int, C: int) -> None:
        queue = deque()
        queue.append((r,c,1))
        # visited = set()

        while queue:
            r, c, d = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0 or grid[r][c] == -1 or grid[r][c] <= d: # (r,c) in visited:
                continue

            grid[r][c] = min(d, grid[r][c])
            # visited.add((r,c))

            queue.append((r+1, c, d+1))
            queue.append((r-1, c, d+1))
            queue.append((r, c+1, d+1))
            queue.append((r, c-1, d+1))
        