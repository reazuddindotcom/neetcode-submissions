# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Node:
#     def __init__(self, node):
#         self.node = node

#     def __lt__(self, other):
#         return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        i = 0
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, (node.val, i, node))
            i += 1

        head = cur = ListNode()
        while heap:
            val, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1
        
        return head.next