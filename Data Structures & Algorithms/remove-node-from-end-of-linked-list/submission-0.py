# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n <= 0:
            return None
        
        fast = head
        i = 0
        while i < n and fast:
            fast = fast.next
            i += 1

        if i < n:
            return None

        slow = ListNode()
        slow.next = head

        while fast:
            fast = fast.next
            slow = slow.next

        if slow.next == head:
            return slow.next.next

        slow.next = slow.next.next

        return head
        

        

        