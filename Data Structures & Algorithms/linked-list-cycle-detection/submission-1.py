# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        first = head
        second = head
        while second:
            first = first.next
            second = second.next
            if not second:
                return False
            second = second.next

            if first == second:
                return True

        return False
        