class DSU:
    def __init__(self):
        self.parents = {}

    def find(self,n):
        if n not in self.parents:
            return n
        return self.find(self.parents[n])
    def union(self,a,b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return False

        self.parents[pa] = pb
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for x,y in edges:
            if not dsu.union(x,y):
                return [x,y]
        return None