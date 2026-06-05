"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        queue = deque()
        created = {} # defaultdict(Node)

        node_copy = Node(node.val)
        created[node.val] = node_copy
        queue.append(node)
        print(node.val, node_copy.val)

        while queue:
            n = queue.popleft()
            new_n = created[n.val]
            print(n.val)
            for neigh in n.neighbors:
                print("-", neigh.val)
                if neigh.val not in created:
                    created[neigh.val] = Node(neigh.val)
                    queue.append(neigh)

                new_n.neighbors.append(created[neigh.val])

        return node_copy
        