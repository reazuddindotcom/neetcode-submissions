class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Q Can I modify the stones
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            if s1 - s2 != 0:
                heapq.heappush(stones, -abs(s1-s2))

        return 0 if not stones else -stones[0]