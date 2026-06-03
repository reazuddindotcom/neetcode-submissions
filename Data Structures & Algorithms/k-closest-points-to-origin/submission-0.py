class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            print(p)
            heapq.heappush(heap, (-(p[0]*p[0] + p[1]*p[1]), p[0], p[1]))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for item in heap:
            result.append([item[1], item[2]])

        return result