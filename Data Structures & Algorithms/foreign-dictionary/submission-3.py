class Solution:
    # Characters without known dependencies should be added as well. 
    # Should've asked.
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ""

        adj_list = defaultdict(set)
        for w in words:
            for c in w:
                adj_list[c] = set()
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            order = self.charOrder(w1, w2)
            if order:
                adj_list[order[0]].add(order[1])

        path = []
        visited = set()
        for c in adj_list:
            print("Start", c)
            cur_visit = set()
            if self.dfs(c, adj_list, path, visited, cur_visit):
                print(path)
                print("Returning")
                return ""
            print(path)

        path.reverse()
        return "".join(path)

    def dfs(self, node: str, adj_list: Dict, path: List[str], visited: Set, cur_visit: Set) -> bool:
        if node in cur_visit:
            print("cycle", node)
            return True

        if node in visited:
            return False

        cur_visit.add(node)

        for ch in adj_list[node]:
            if self.dfs(ch, adj_list, path, visited, cur_visit):
                return True

        cur_visit.remove(node)
        path.append(node)
        visited.add(node)

        
    def charOrder(self, w1: str, w2: str) -> [str, str]:
        result = []
        i = 0
        while i < len(w1) and i < len(w2):
            if w1[i] != w2[i]:
                return [w1[i], w2[i]]
            i += 1

        return result

# WA ["abc","bcd","cde"] --> 1) need to call dfs for all characters, even the unlinked ones
#                        --> 2) add chars to path after the dfs call
# WA ["wrt","wrf","er","ett","rftt","te"] --> use set to avoid duplicates in adjacency list
# WA ["baa","abcd","abca","cab","cad"]