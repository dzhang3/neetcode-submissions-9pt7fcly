# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if not cur1:
            return cur2
        if not cur2:
            return cur1

        head = cur = None
        if cur1 and cur1.val < cur2.val:
            head = cur = cur1
            cur1 = cur1.next
        elif cur2:
            head = cur = cur2
            cur2 = cur2.next

        while cur1 or cur2:
            if (cur1 and cur2 and cur1.val < cur2.val) or not cur2:
                cur.next = cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur2
                cur2 = cur2.next

        
        return head

        