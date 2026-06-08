class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_list = {i: [] for i in range(n+1)} # defaultdict(list) not a good idea
        for edge in edges:
            adj_list[edge[0]].append(edge[1]) # add both directions
            adj_list[edge[1]].append(edge[0]) # but then we have cycle
                                              # keep track of parents
                                              # to avoid going back
        visited = [False]*(n+1)
        cycle = set()
        self.cycle_found(1, -1, adj_list, visited, cycle)

        for i in range(n-1, -1, -1):
            if (edges[i][0], edges[i][1]) in cycle or (edges[i][1], edges[i][0]) in cycle:
                return edges[i]

        return []

    def cycle_found(self, node: int, parent: int, adj_list: map, visited: [], cycle: set) -> [bool, int]:
        if visited[node]:
            cycle.add((parent, node))
            return [True, node]

        visited[node] = True
        for c in adj_list[node]:
            if c == parent:
                continue
            found, st = self.cycle_found(c, node, adj_list, visited, cycle)
            if found:
                print(found, st)
                if st != -1:
                    print("adding", node, c)
                    cycle.add((node, c))
                if st == node: # came back to cycle start
                    return [True, -1]
                else:
                    return [True, st]
                

        return [False, -1]
# TC [[0,1],[0,2],[2,3],[2,4],[4,5],[4,6],[2,1],[1,0]]
# WA [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]