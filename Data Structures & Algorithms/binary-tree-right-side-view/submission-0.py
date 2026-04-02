# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        parent = deque()
        parent.append(root)
        while parent:
            children = deque()
            while parent:
                node = parent.popleft()
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
                if not parent:
                    res.append(node.val)
            parent = children
        return res