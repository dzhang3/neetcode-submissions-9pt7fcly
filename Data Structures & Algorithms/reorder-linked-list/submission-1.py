# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        head2 = slow.next if fast else slow
        cur2 = head2.next
        head2.next = None
        while cur2:
            temp = cur2.next
            cur2.next = head2
            head2 = cur2
            cur2 = temp

        cur1 = head
        cur2 = head2

        while cur2:
            temp1 = cur1.next
            temp2 = cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2
        
        if cur1:
            cur1.next = None
        

        