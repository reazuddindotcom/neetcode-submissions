class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda pair: pair[0])
        result = []
        i = 0
        while i < len(intervals):
            ival = intervals[i]
            i += 1
            while i < len(intervals) and ival[1] >= intervals[i][0]:
                ival[1] = max(ival[1], intervals[i][1])
                i += 1

            result.append(ival)

        return result


        