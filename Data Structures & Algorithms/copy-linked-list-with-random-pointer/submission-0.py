"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None: None}
        new_head = Node(0)
        old = head
        new = new_head
        while old:
            temp = Node(old.val)
            new.next = temp

            new = temp
            node_map[old] = new
            old = old.next

        new = new_head.next
        old = head
        while new:
            new.random = node_map[old.random]

            new = new.next
            old = old.next


        return new_head.next