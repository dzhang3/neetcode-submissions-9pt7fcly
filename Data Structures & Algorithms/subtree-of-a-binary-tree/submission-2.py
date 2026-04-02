# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(r1,r2):
            if not r1 and not r2:
                return True
            if r1 and r2 and r1.val == r2.val:
                return isSameTree(r1.left,r2.left) and isSameTree(r1.right,r2.right)
            else:
                return False

        queue = deque()
        queue.append(root)
        sameSub = False
        while queue:
            cur = queue.popleft()
            if not cur:
                continue
            queue.append(cur.left)
            queue.append(cur.right)
            sameSub = sameSub or isSameTree(cur, subRoot)
        return sameSub