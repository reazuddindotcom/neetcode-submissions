class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if not self.left_max and not self.right_min:
            heapq.heappush(self.left_max, -num)
            return

        if (-self.left_max[0]) >= num:
            heapq.heappush(self.left_max, -num)
        else:
            heapq.heappush(self.right_min, num)

        left_size = len(self.left_max)
        right_size = len(self.right_min)
        while left_size - 1 > right_size:
            item = heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, -item)
            left_size -= 1
            right_size += 1


        while left_size < right_size:
            item = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -item)
            left_size += 1
            right_size -= 1

    def findMedian(self) -> float:
        if not self.left_max and not self.right_min:
            return None

        if len(self.left_max) == len(self.right_min):
            return ((-self.left_max[0]) + self.right_min[0]) / 2

        return -self.left_max[0]
        
        