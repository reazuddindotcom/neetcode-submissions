class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        # dist_map = {}
        for e in times:
            # assume no duplicates
            # if e[0] not in adj_list:
            #     adj_list[e[0]] = []
            adj_list[e[0]].append((e[1],e[2]))
            # dist_map[(e[0],e[1])] = e[2]

        pq = []
        heapq.heappush(pq, (0, k))
        visited = set()
        min_t = 0
        while pq:
            t, u = heapq.heappop(pq)
            if u in visited:
                continue
            min_t = max(min_t, t)
            print("popped: ", u, t, min_t)
            for v,ti in adj_list[u]:
                heapq.heappush(pq, (t+ti, v))
                
            visited.add(u)

        if len(visited) != n:
            return -1

        return min_t
