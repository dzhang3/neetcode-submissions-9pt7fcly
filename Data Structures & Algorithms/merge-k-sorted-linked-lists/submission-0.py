# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        n = 0
        for l in lists:
            if l:
                n += 1

        while n > 0:
            minIndex = 0
            minVal = float('inf')        
            for index,node in enumerate(lists):
                if node and node.val < minVal:
                    minVal = node.val
                    minIndex = index
            
            cur.next = ListNode(val=minVal)
            lists[minIndex] = lists[minIndex].next
            if lists[minIndex] is None:
                n -= 1
            cur = cur.next
        
        return dummy.next