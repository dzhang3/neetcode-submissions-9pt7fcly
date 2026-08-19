class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) * len(matrix[0])
        l,r = 0,n-1
        # print(n)
        while l <= r:
            m = (l + r) // 2
            x,y = m // len(matrix[0]), m % len(matrix[0])
            # print(l,r,m,x,y,matrix[x][y])
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = m + 1
            else:
                r = m - 1
        return False