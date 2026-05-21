class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        heap = []
        for v in freq.keys():
            heapq.heappush(heap, (freq[v], v))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
#        for i in range(k):
#            ans.append(heapq.heappop(heap)[1])
        for i in heap:
            ans.append(i[1])

        return ans