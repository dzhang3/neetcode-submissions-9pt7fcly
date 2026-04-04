class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(i,j):
            if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            total = 1
            for dx, dy in dirs:
                total += dfs(i + dx, j + dy)
            return total
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ans = max(ans,dfs(i,j))
        return ans
