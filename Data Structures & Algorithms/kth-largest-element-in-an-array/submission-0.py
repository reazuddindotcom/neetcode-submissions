class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # duplicates in the array ?
        result = []
        for n in nums:
            heapq.heappush(result, n)
            if len(result) > k:
                heapq.heappop(result)

        return result[0]