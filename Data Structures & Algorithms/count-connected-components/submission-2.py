class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    
    def find(self,n):
        if self.parents[n] != n:
            return self.find(self.parents[n])
        return n
    
    def union(self,a,b):
        pa, pb = self.find(a),self.find(b)
        if pa == pb:
            return False
        self.parents[pa] = pb
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for a,b in edges:
            if dsu.union(a,b):
                res -= 1
        
        return res