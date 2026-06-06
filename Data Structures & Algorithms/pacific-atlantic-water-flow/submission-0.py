class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # from every cell start BFS/DFS.
        # record reachability for each cell went through
        # repeat from next un-searched cell
        # Above is brute force. Followin the hints.
        R = len(heights)
        if not R:
            return 0
        C = len(heights[0])

        # BFS from Pacific
        pacific = [[False] * C for r in range(R)]
        queue = deque()
        for r in range(R):
            queue.append((r,0))
        for c in range(C):
            queue.append((0,c))

        while queue:
            r, c = queue.popleft()
    
            # track visited
            pacific[r][c] = True
            if r+1 >=0 and r+1 < R and heights[r][c] <= heights[r+1][c] and not pacific[r+1][c]:
                queue.append((r+1, c))
            if r-1 >=0 and r-1 < R and heights[r][c] <= heights[r-1][c] and not pacific[r-1][c]:
                queue.append((r-1, c))
            if c+1 >=0 and c+1 < C and heights[r][c] <= heights[r][c+1] and not pacific[r][c+1]:
                queue.append((r, c+1))
            if c-1 >=0 and c-1 < C and heights[r][c] <= heights[r][c-1] and not pacific[r][c-1]:
                queue.append((r, c-1))
                
        # BFS from Atlantic
        atlantic = [[False] * C for r in range(R)]
        queue = deque()
        for r in range(R):
            queue.append((r,C-1))
        for c in range(C):
            queue.append((R-1,c))

        while queue:
            r, c = queue.popleft()
    
            # track visited
            atlantic[r][c] = True
            if r+1 >=0 and r+1 < R and heights[r][c] <= heights[r+1][c] and not atlantic[r+1][c]:
                queue.append((r+1, c))
            if r-1 >=0 and r-1 < R and heights[r][c] <= heights[r-1][c] and not atlantic[r-1][c]:
                queue.append((r-1, c))
            if c+1 >=0 and c+1 < C and heights[r][c] <= heights[r][c+1] and not atlantic[r][c+1]:
                queue.append((r, c+1))
            if c-1 >=0 and c-1 < C and heights[r][c] <= heights[r][c-1] and not atlantic[r][c-1]:
                queue.append((r, c-1))

        result = []
        for r in range(R):
            for c in range(C):
                if atlantic[r][c] and pacific[r][c]:
                    result.append([r, c])

        return result