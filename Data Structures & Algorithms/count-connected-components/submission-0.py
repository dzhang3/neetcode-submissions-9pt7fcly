class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in neighbors[node]:
                dfs(neighbor)
        
        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans