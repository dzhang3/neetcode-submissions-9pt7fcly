class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = []
        colSets = []
        boxSets = []

        for _ in range(9):
            rowSets.append(set())
            colSets.append(set())
            boxSets.append(set())

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = board[row][col]
                    boxRow = row // 3
                    boxCol = col // 3
                    boxIndex = boxRow * 3 + boxCol
                    if num in boxSets[boxIndex] or num in rowSets[row] or num in colSets[col]:
                        return False

                    boxSets[boxIndex].add(num)
                    rowSets[row].add(num)
                    colSets[col].add(num)

        return True
                    