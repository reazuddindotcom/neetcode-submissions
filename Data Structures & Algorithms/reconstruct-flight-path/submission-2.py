class Solution:
    # V0: Regular solution, not hierholzer's algorithm --> Got TLE
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for e in tickets:
            adj_list[e[0]].append(e[1])

        for l in adj_list:
            adj_list[l].sort()

        # print(adj_list)
        path = ["JFK"]
        # Use a list of counts or index-based tracking because tickets can be duplicates
        adj_map = {src: [dest, [False] * len(dest)] for src, dest in adj_list.items()}
        
        if self.dfs(adj_map, "JFK", path, len(tickets)+1):
            return path

        return []

    def dfs(self, adj_map: Dict, node: str, path: List[str], n: int) -> bool:
        if len(path) == n:
            return True

        if node not in adj_map:
            return False

        neighbors, used = adj_map[node]
        for i in range(len(neighbors)):
            if not used[i]:
                used[i] = True
                path.append(neighbors[i])
                if self.dfs(adj_map, neighbors[i], path, n):
                    return True
                path.pop()
                used[i] = False


        return False


# WA [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# TLE [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
        