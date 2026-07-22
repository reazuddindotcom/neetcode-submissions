class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # m = len(obstacleGrid)
        # if m == 0:
        #     return 0
        # n = len(obstacleGrid[0])
        # if obstacleGrid[0][0] == 1:
        #     return 0
        # dist = [[0] * (n+1) for _ in range(m+1)]
        # dist[m-1][n-1] = 1
        # print(dist)
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if (i == m-1 and j == n-1) or obstacleGrid[i][j] == 1:
        #             continue
        #         # dist at dest is 1
        #         dist[i][j] = dist[i+1][j] + dist[i][j+1]

        # return dist[0][0]

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        # dist[i+1][j+1] corresponds to cell (i,j)
        dist = [[0] * (n + 1) for _ in range(m + 1)]
        dist[1][1] = 1  # base case: one way to stand at start

        for i in range(1,m+1,1):
            for j in range(1,n+1,1):
                if i == 1 and j == 1:
                    continue  # already set
                if obstacleGrid[i-1][j-1] == 1:
                    dist[i][j] = 0
                else:
                    # dist[i+1][j+1] = dist[i][j+1] (up) + dist[i+1][j] (left)
                    dist[i][j] = dist[i-1][j] + dist[i][j-1]

        return dist[m][n]