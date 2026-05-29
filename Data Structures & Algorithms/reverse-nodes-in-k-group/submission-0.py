# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur:
            kth = cur
            for i in range(k):
                if kth:
                    kth = kth.next
            if not kth:
                break;

            next = kth.next

            kth.next = None
            rev_head = self.reverseList(cur.next)
            rev_tail = cur.next
            print(kth.val, rev_head.val, rev_tail.val)

            cur.next.next = next
            cur.next = rev_head
            cur = rev_tail

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        prev = None
        cur = head
        temp = head.next
        while temp:
            cur.next = prev
            prev = cur
            cur = temp
            temp = temp.next

        cur.next = prev

        return cur 


