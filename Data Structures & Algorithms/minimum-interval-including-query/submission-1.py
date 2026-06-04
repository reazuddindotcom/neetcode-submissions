class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return []

        if not queries:
            return []

        i_len = len(intervals)
        q_len = len(queries)
        i = 0
        q = 0

        input_queries = list(queries)
        intervals.sort()
        queries.sort()
        map = {}

        heap = []
        while q < q_len: # i < i_len and 
            while i < i_len and intervals[i][1] < queries[q]:
                i += 1

            while i < i_len and intervals[i][0] <= queries[q]:
                val = intervals[i]
                heapq.heappush(heap, ((val[1]-val[0]+1), val[0], val[1]))
                i += 1

            # print(queries[q], heap[0][2])
            while heap and heap[0][2] < queries[q]:
                print(queries[q], heap)
                heapq.heappop(heap)
                print("-----------")
            print(heap)

            if heap:
                map[queries[q]] = min((map.get(queries[q], float("inf"))), heap[0][0])
            # print("Q", map.get(queries[q], float("inf")), i, q)
            q += 1
            print(i, q)
            print("===============")

        # print("TheMap: ", map)
        result = []
        for query in input_queries:
            if query not in map:
                result.append(-1)
            else:
                result.append(map[query])
            # print("  ", result)

        return result
            

