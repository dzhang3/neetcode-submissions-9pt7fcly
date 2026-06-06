class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self,n):
        if self.parents[n] != n:
            return self.find(self.parents[n])
        else:
            return n
        
    def union(self,a,b):
        pa, pb = self.find(a),self.find(b)
        self.parents[pa] = pb
        self.sizes[pb] += self.sizes[pa]

    def connected(self,a,b):
        pa, pb = self.find(a),self.find(b)
        return pa == pb


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles?
        dsu = DSU(n)
        for a,b in edges:
            if dsu.connected(a,b):
                return False
            dsu.union(a,b)
        
        return dsu.sizes[dsu.find(0)] == n