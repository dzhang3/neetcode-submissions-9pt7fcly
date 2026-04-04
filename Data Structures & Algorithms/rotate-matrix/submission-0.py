class Solution:
    def rotate(self, grid: List[List[int]]) -> None:
        n = len(grid)
        for i in range(n // 2):
            for j in range(i,n - 1 - i):
                temp = grid[j][n - 1 - i]
                grid[j][n - 1 - i] = grid[i][j]
                grid[n - 1 - i][n - 1 - j],temp = temp,grid[n - 1 - i][n - 1 - j]
                grid[n - 1 - j][i],temp = temp,grid[n - 1 - j][i]
                grid[i][j] = temp
        
                