# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        r1 = r2 = head
        i = 0
        while r2:
            if i != 0 and r1 == r2:
                return True
            r1 = r1.next
            if r2.next:
                r2 = r2.next.next
            else:
                r2 = None
            i += 1
        return False