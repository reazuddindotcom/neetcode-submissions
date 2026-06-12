class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # compute pair wise distance
        # - O(n2)
        # put then in PQ or sort
        # pick the smallest one and connect
        # - Is this guaranteed to give me the min cost?
        # - Yes, proof by counter example.
        # How do we avoid circle ??
        # - Every time we connect do a dfs
        # - Anything more efficient ?
        # Use KRUSKAL's or PRIM's algorithm

        adj_list = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue

                x = points[i]
                y = points[j]
                d = abs(x[0]-y[0]) + abs(x[1]-y[1])
                adj_list[i].append((d, j))
                adj_list[j].append((d, i))

        pq = []
        pq.append((0,0))
        visited = set()
        cost = 0
        while pq:
            d, n = heapq.heappop(pq)
            if n in visited:
                continue
            cost += d
            for ch in adj_list[n]:
                heapq.heappush(pq, ch)

            visited.add(n)
            if len(visited) == len(points):
                break

        return cost


                
        