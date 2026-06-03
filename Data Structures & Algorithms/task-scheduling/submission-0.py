class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Q: Completion order matters ??
        map = {}
        for t in tasks:
            map[t] = map.get(t, 0) + 1
        # print("map", map)

        heap = []
        for t in map:
            heapq.heappush(heap, -map[t])
        # print("heap", heap)

        q = deque()
        time = 0
        while heap or q:
            # print("time", time)
            t = heapq.heappop(heap)
            t += 1 # decreament the count

            if t:
                q.append((t, time+n+1))
                # print("Q", q)
            
            time += 1

            if not heap and q:
                time = q[0][1]
                # print("time", time)

            while q and q[0][1] <= time:
                next = q.popleft()
                heapq.heappush(heap, next[0])
            # print("heap", heap)
            # print("----")

        return time




