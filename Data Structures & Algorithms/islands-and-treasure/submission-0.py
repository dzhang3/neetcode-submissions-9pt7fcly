class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        r,c = len(grid),len(grid[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(i,j):
            queue = deque()
            queue.append((i,j,0))
            while queue:
                x,y,d = queue.popleft()
                print(x,y,d)
                grid[x][y] = d
                for dx,dy in dirs:
                    if x + dx >= 0 and x + dx < r and y + dy >= 0 and y + dy < c and grid[x+dx][y+dy] > d:
                        queue.append((x+dx,y+dy,d+1))
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    bfs(i,j)
        
                