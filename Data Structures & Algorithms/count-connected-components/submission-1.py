class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
    
    def find(self,n):
        if self.parents[n] != n:
            return self.find(self.parents[n])
        return n
    
    def union(self,a,b):
        pa, pb = self.find(a),self.find(b)
        self.parents[pa] = pb

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for a,b in edges:
            dsu.union(a,b)
        
        ans = []
        for p in dsu.parents:
            ans.append(dsu.find(p))
        
        return len(set(ans))