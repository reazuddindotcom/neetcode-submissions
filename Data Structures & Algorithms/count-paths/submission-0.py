class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Q: distance at destination - 0 or 1 ?

        dist = [[0] * (n+1) for _ in range(m+1)]
        dist[m-1][n-1] = 1
        print(dist)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                # dist at dest is 1
                dist[i][j] = dist[i+1][j] + dist[i][j+1]

        return dist[0][0]


        