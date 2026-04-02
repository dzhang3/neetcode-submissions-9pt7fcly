# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def height(root):
            nonlocal diameter
            if not root:
                return -1
            l = height(root.left)
            r = height(root.right)
            diameter = max(l + r + 2, diameter)
            return max(l, r) + 1
        height(root)
        return diameter
        