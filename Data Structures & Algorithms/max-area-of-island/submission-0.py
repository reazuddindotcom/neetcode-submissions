class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])

        area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = max(area, self.bfs(grid,r,c,R,C))
                    print(r,c, area)

        return area
    
    def bfs(self, grid: List[List[str]], r: int, c: int, R: int, C: int) -> int:
        queue = deque()
        queue.append((r,c))

        area = 0
        while queue:
            r, c = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                continue

            grid[r][c] = 0 # visited (or flooded)
            area += 1

            queue.append((r+1, c))
            queue.append((r-1, c))
            queue.append((r, c+1))
            queue.append((r, c-1))

        return area
       