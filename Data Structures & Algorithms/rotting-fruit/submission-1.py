class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lastMin = 0
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        r,c = len(grid),len(grid[0])
        mins = [[-1] * c for _ in range(r)]

        if max([max(row) for row in grid]) == 0:
            return 0

        def bfs(i,j):
            minute = 0
            queue = deque()
            queue.append((i,j))

            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    mins[x][y] = minute
                    for dx, dy in dirs:
                        if x + dx >= 0 and x + dx < r and y + dy >= 0 and y + dy < c and grid[x + dx][y + dy] == 1 and (mins[x + dx][y + dy] == -1 or mins[x + dx][y + dy] > minute):
                            queue.append((x+dx,y+dy))
                minute += 1
        hasOrange = False
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    bfs(i,j)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and mins[i][j] == -1:
                    return -1
        
        return max([max(row) for row in mins])


