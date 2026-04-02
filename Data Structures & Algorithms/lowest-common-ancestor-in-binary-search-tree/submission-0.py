# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None
        def dfs(root):
            nonlocal p,q, lca
            if not root:
                return False
            l = dfs(root.left)
            r = dfs(root.right)

            if root.val == p.val or root.val == q.val:
                if l or r:
                    lca = root
            else:
                if l and r:
                    lca = root
            return l or r or root.val == p.val or root.val == q.val
        dfs(root)
        return lca
            

        