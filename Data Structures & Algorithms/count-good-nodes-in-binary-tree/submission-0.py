# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def dfs(node,maxVal):
            if not node:
                return
            nonlocal goodNodes
            if not maxVal > node.val:
                goodNodes += 1
            dfs(node.left,max(node.val,maxVal))
            dfs(node.right,max(node.val,maxVal))
        dfs(root, root.val)
        return goodNodes
        