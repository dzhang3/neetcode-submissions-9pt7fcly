# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        c1 = l1
        c2 = l2
        dummy = ListNode()
        prev = dummy
        while c1 or c2 or carry:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0
            dsum = v1 + v2 + carry
            carry = 0
            if dsum >= 10:
                carry = 1
                dsum -= 10
            newNode = ListNode(val=dsum)
            prev.next = newNode
            prev = newNode
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next

        return dummy.next
        
        
