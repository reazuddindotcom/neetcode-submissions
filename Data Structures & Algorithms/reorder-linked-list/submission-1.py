# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #print(head.val) if head else print(head)
        if not head:
            return

        slow = head
        fast = head.next
        temp = fast
        print(slow.val) if slow else print(slow)
        print(fast.val) if fast else print(fast)
        while fast and fast.next:
            slow = slow.next
            temp = fast.next
            fast = fast.next.next
            print(slow.val) if slow else print(slow)
            print(fast.val) if fast else print(fast)
            print("------------")


        print("===========")
        if not fast:
            fast = temp
        print(slow.val) if slow else print(slow)
        print(fast.val) if fast else print(fast)

        # if not fast or head.next == fast: # 1 or 2 element
        #     return

        list2 = self.reverseList(slow.next)
        slow.next = None
        print(list2.val) if list2 else print(list2)

        list1 = head
        print(list1.val) if list1 else print(list1)
        print("===========")
        while list2:
            temp1 = list1.next
            list1.next = list2

            temp2 = list2
            list2 = list2.next
            list1 = temp1
            temp2.next = temp1
            print(list1.val) if list1 else print(list1)
            print(list2.val) if list2 else print(list2)
            print("------------")

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print("reverse")
        print(head.val) if head else print(head)
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


        