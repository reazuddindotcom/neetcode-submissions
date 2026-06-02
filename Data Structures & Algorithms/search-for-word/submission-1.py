class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        if not R:
            return False
        C = len(board[0])

        for r in range(R):
            for c in range(C):
                if self.dfs(board, r, c, R, C, word, 0):
                    return True

        return False

    def dfs(self, board: List[List[str]], r, c, R, C, word: str, i: int) -> bool:
        if r < 0 or c < 0 or r >= R or c >= C or i >= len(word) or board[r][c] != word[i]:
            return False

        if i == len(word) - 1:
            return True

        board[r][c] = "*" # visited
        if self.dfs(board, r+1, c, R, C, word, i+1):
            return True
        if self.dfs(board, r-1, c, R, C, word, i+1):
            return True
        if self.dfs(board, r, c+1, R, C, word, i+1):
            return True
        if self.dfs(board, r, c-1, R, C, word, i+1):
            return True

        board[r][c] = word[i]

        return False

        