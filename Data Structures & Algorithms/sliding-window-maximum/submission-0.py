class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        heap = []
        l = 0
        r = k - 1
        for i in range(0, k-1, 1):
            heapq.heappush(heap, (-nums[i],i))

        res = []
        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))

            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            
            res.append(-heap[0][0])
            l += 1
            r += 1

        return res

