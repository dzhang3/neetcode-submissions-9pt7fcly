# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur1 = head
        cur2 = head
        for _ in range(n):
            cur2 = cur2.next
        
        prev = None
        while cur2:
            prev = cur1
            cur1 = cur1.next
            cur2 = cur2.next
        
        # remove node
        if prev:
            prev.next = cur1.next
            return head
        else:
            return head.next