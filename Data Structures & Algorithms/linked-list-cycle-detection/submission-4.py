# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r1 = r2 = head
        i = 0
        while r2 and r2.next:
            r1 = r1.next
            r2 = r2.next.next
            if r1 == r2:
                return True
        return False