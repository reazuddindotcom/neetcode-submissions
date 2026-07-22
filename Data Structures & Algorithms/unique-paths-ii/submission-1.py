class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        dist = [[0] * (n+1) for _ in range(m+1)]
        dist[m-1][n-1] = 1
        print(dist)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i == m-1 and j == n-1) or obstacleGrid[i][j] == 1:
                    continue
                # dist at dest is 1
                dist[i][j] = dist[i+1][j] + dist[i][j+1]

        return dist[0][0]