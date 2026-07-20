class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqrs = defaultdict(set)
        for i in range(9):
            rset = set()
            cset = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in rset:
                    # print("row false: ",board[i][j],rset)
                    return False
                if board[j][i] != "." and board[j][i] in cset:
                    # print("col false: ",board[j][i],cset)
                    return False
                rset.add(board[i][j])
                cset.add(board[j][i])

                if board[i][j] != "." and board[i][j] in sqrs[(i // 3, j // 3)]:
                    # print("sqr false")
                    return False
                sqrs[(i // 3, j // 3)].add(board[i][j])
        return True

