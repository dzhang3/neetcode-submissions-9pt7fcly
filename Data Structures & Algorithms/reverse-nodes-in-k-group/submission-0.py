# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseSingleList(self, head):
        cur = head
        last = head
        newHead = None
        while cur:
            tmp = cur.next
            cur.next = newHead

            newHead = cur
            cur = tmp
        return (newHead, last)




    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        start = head
        end = head
        dummy = ListNode()
        prev = dummy
        while end:
            i = 1
            while i < k and end.next:
                end = end.next
                i += 1
            if i != k:
                break

            nextHead = end.next
            end.next = None
            newStart, newEnd = self.reverseSingleList(start)
            prev.next = newStart
            prev = newEnd
            newEnd.next = nextHead         
            start = end = nextHead
        return dummy.next   


        