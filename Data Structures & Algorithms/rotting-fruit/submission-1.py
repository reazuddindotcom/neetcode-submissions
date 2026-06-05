class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        if not R:
            return 0
        C = len(grid[0])

        queue = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r+1,c,1))
                    queue.append((r-1,c,1))
                    queue.append((r,c+1,1))
                    queue.append((r,c-1,1))

        INF = 1000
        dist = [[INF] * C for r in range(R)]

        while queue: # track visited
            r,c,d = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != 1 or dist[r][c] <= d:
                continue

            dist[r][c] = min(d, dist[r][c])

            queue.append((r+1,c,d+1))
            queue.append((r-1,c,d+1))
            queue.append((r,c+1,d+1))
            queue.append((r,c-1,d+1))

        # print(dist)
        
        min_req = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    min_req = max(min_req, dist[r][c])


        if min_req == 1000:
            return -1
        return min_req