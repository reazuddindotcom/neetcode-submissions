class Solution:
    def __init__(self):
        self.results = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [["."]*n]*n
        board = [["."] * n for i in range(n)]
        print(board)
        print("---")

        self.results = []
        self.backtrack(board, 0, n, set(), set(), set(), set())

        return self.results
        
    def backtrack(self, board: List[List[str]], r: int, n: int, rows: set, cols: set, p_diag: set, n_diag: set) -> None:
        if r == n:
            self.results.append(self.serialize(board))
            return

        for c in range(n):
            if self.isSafe(r,c,rows,cols,p_diag,n_diag):
                rows.add(r)
                cols.add(c)
                p_diag.add(r+c)
                n_diag.add(r-c)

                board[r][c] = "Q"

                self.backtrack(board, r+1, n, rows, cols, p_diag, n_diag)

                board[r][c] = "."

                rows.remove(r)
                cols.remove(c)
                p_diag.remove(r+c)
                n_diag.remove(r-c)

    def isSafe(self, r: int, c: int, rows: set, cols: set, p_diag: set, n_diag: set) -> bool:
        if r in rows or c in cols or r+c in p_diag or r-c in n_diag:
            return False

        return True

    def serialize(self, board: List[List[str]]) -> List[str]:
        l = []
        print(board)
        for r in board:
            l.append(''.join(r))

        return l
