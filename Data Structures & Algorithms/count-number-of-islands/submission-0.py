class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        visited = [[False] * c for _ in range(r)]
        
        def dfs(i,j):
            visited[i][j] = True
            if i < r - 1 and grid[i + 1][j] == '1' and not visited[i + 1][j]:
                dfs(i + 1,j)
            if i > 0 and grid[i - 1][j] == '1' and not visited[i - 1][j]:
                dfs(i - 1,j)
            if j < c - 1 and grid[i][j + 1] == '1' and not visited[i][j + 1]:
                dfs(i,j + 1)
            if j > 0 and grid[i][j - 1] == '1' and not visited[i][j - 1]:
                dfs(i,j - 1)
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i,j)
                    ans += 1
        return ans
