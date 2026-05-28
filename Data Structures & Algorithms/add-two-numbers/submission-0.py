# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        res_head = ListNode()
        cur = res_head
        d1 = l1 # COPY NOT NEEDED
        d2 = l2 # COPY NOT NEEDED
        c = 0
        while d1 or d2 or c:
            val1, val2 = 0, 0
            if d1:
                val1 = d1.val
                d1 = d1.next
            if d2:
                val2 = d2.val
                d2 = d2.next

            val = val1 + val2 + c
            r = val % 10
            c = val // 10

            cur.next = ListNode(r)
            cur = cur.next

        return res_head.next
        

        
