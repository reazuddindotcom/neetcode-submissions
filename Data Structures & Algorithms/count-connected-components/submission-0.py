class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(n)} # defaultdict(list) not a good idea
        for edge in edges:
            adj_list[edge[0]].append(edge[1]) # add both directions
            adj_list[edge[1]].append(edge[0]) # but then we have cycle
                                              # keep track of parents
                                              # to avoid going back
        comp = 0
        visited = [False]*n
        for node in adj_list:
            if not visited[node]:
                comp += 1
                self.dfs(node, -1, adj_list, visited)

        return comp

    def dfs(self, node: int, parent: int, adj_list: map, visited: []) -> None:
        if visited[node]:
            return

        visited[node] = True
        for c in adj_list[node]:
            if c == parent:
                continue
            self.dfs(c, node, adj_list, visited)