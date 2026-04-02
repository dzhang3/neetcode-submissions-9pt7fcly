"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        cur = head
        dummy = Node(0)
        prev = dummy
        while cur is not None:
            newNode = Node(cur.val)
            nodes[cur] = newNode
            prev.next = newNode
            
            cur = cur.next
            prev = newNode
        
        cur2 = dummy.next
        cur = head
        while cur is not None:
            cur2.random = nodes[cur.random] if cur.random is not None else None
            cur = cur.next
            cur2 = cur2.next
        
        return dummy.next
            