class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(i,j,o,visited):
            o.add((i,j))
            visited[i][j] = True
            for dx, dy in dirs:
                if i + dx >= 0 and i + dx < n and j + dy >= 0 and j + dy < m and heights[i + dx][j + dy] >= heights[i][j] and not visited[i + dx][j + dy]:
                    dfs(i + dx,j + dy,o,visited)

        po = set()
        ao = set()

        pvisited = [[False] * m for _ in range(n)]
        avisited = [[False] * m for _ in range(n)]
        for i in range(n):
            dfs(i,0,po,pvisited)
            dfs(i,m-1,ao,avisited)
        
        for j in range(m):
            dfs(0,j,po,pvisited)
            dfs(n-1,j,ao,avisited)
        
        return list(po & ao)