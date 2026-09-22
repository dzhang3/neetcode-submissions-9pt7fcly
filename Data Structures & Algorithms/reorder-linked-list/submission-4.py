# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        r1 = r2 = head
        while r2 and r2.next and r2.next.next:
            r1 = r1.next
            r2 = r2.next.next

        h1 = head
        h2 = r1.next
        r1.next = None

        # print(h2.val)
        prev = None
        cur = h2
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        h2 = prev
        
        while h1 and h2:
            t1 = h1.next
            t2 = h2.next
            h1.next = h2
            h2.next = t1

            h1 = t1
            h2 = t2
        