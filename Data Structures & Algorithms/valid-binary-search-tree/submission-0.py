# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        def validateBST(node):
            nonlocal isValid
            if not node:
                return (float('inf'),float('-inf'))
            minl, maxl = validateBST(node.left)
            minr, maxr = validateBST(node.right)
            if node.val <= maxl or node.val >= minr:
                isValid = False
            return (min(minl,minr,node.val),max(maxl,maxr,node.val))
        validateBST(root)
        return isValid
        