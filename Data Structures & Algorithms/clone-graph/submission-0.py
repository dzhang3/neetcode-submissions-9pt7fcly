"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = {}
        def clone(node):
            neighbors = []
            nodes[node.val] = Node(node.val)
            for n in node.neighbors:
                if n.val in nodes:
                    neighbors.append(nodes[n.val])
                else:
                    neighbors.append(clone(n))
            nodes[node.val].neighbors = neighbors
            return nodes[node.val]
        return clone(node)