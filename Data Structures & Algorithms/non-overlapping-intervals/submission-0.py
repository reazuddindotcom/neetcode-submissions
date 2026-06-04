class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        lastEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals), 1):
            if lastEnd > intervals[i][0]:
                count += 1
                lastEnd = min(lastEnd, intervals[i][1]) # letting the max one go
            else:
                lastEnd = intervals[i][1]

        return count