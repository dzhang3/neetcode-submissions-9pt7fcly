class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l,r = 0, m * n - 1
        while l <= r:
            m = round((l + r) / 2)
            x = m // n
            y = m % n
            if target > matrix[x][y]:
                l = m + 1
            elif target < matrix[x][y]:
                r = m - 1
            else:
                return True
        return False