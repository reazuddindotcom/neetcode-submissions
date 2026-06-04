class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        result = []
        # if newInterval[1] < intervals[0][0]:
        #     result.append(newInterval)

        l = len(intervals)
        i = 0
        while i < l:
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            else:
                break
            print(i)
            i += 1
        print(i)

        if i == l:
            result.append(newInterval)
            return result

        print("here")
        if newInterval[0] < intervals[i][1] or newInterval[1] > intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
        while i < l and newInterval[1] >= intervals[i][0]:
            #newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)
        while i < l:
            result.append(intervals[i])
            i += 1

        return result
        

    # Bineary Search Doesn't make it any efficient
    # def binSearch(self, intervals: List[List[int]], val: int) -> int:
    #     r = 0
    #     l = len(intervals)-1

    #     while l <= r:
    #         m = l + (l-r) // 2
    #         if intervals[m][0] == val:
    #             return m

    #         if intervals[m][0] < val:
    #             l = m + 1
    #         else: 
    #             r = m - 1