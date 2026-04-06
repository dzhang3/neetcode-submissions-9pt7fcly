class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(0,-1),(1,0),(0,1)]
        r,c = len(grid),len(grid[0])
        fresh = 0

        minute = 0
        queue = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        while fresh > 0 and queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in dirs:
                    if x + dx >= 0 and x + dx < r and y + dy >= 0 and y + dy < c and grid[x + dx][y + dy] == 1:
                        queue.append((x+dx,y+dy))
                        grid[x + dx][y + dy] = 2
                        fresh -= 1
            minute += 1
        
        return minute if fresh == 0 else -1


