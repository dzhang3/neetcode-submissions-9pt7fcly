class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix), len(matrix[0])

        top = False
        for i in range(r):
            if matrix[i][0] == 0:
                top = True
                break
        
        side = False
        for j in range(c):
            if matrix[0][j] == 0:
                side = True
                break

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,r):
            if matrix[i][0] == 0:
                for j in range(1,c):
                    matrix[i][j] = 0
        
        for j in range(1,c):
            if matrix[0][j] == 0:
                for i in range(1,r):
                    matrix[i][j] = 0
        
        if side:
            for j in range(c):
                matrix[0][j] = 0
        
        if top:
            for i in range(r):
                matrix[i][0] = 0

        