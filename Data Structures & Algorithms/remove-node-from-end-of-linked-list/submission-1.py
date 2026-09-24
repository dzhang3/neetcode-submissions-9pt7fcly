# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        cur = head
        end = head
        while end:
            if n <= 0:
                prev = cur
                cur = cur.next
            end = end.next
            n -= 1
        prev.next = cur.next
        return dummy.next