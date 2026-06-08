class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Q: Can the input be a forest as well?
        # Q: Is each pair appearing only once?
        # DFS from all un-visited nodes
        print("Hello")
        if len(edges) != n-1:
            print("len", len(edges))
            return False

        adj_list = {i: [] for i in range(n)} # defaultdict(list)
        for edge in edges:
            adj_list[edge[0]].append(edge[1]) # no duplicate input
            adj_list[edge[1]].append(edge[0]) # but then we have cycle
                                              # keep track of parents
                                              # to avoid going back

        visited = [False]*n
        # DON'T start dfs from every node. The tree should be connected
        # So just starting with one node should cover all
        is_tree = self.dfs(0, -1, adj_list, visited)
        if is_tree:
            for v in visited:
                if not v:
                    print("not visited", v)
                    return False
            return True
        else:
            return False

    def dfs(self, node: int, parent: int, adj_list: map, visited: []) -> bool:
        if visited[node]:
            print("visited", node)
            return False

        visited[node] = True
        for c in adj_list[node]:
            if c == parent:
                continue
            if not self.dfs(c, node, adj_list, visited):
                print("dfs", node)
                return False

        return True

# WA, n=5, edges=[[0,1],[2,0],[3,0],[1,4]]