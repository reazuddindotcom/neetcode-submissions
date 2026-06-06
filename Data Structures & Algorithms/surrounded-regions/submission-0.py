class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        if not R:
            return 0
        C = len(board[0])

        queue = deque()
        for r in range(R):
            if board[r][0] == "O":
                queue.append((r,0))
            if board[r][C-1] == "O":
                queue.append((r,C-1))

        for c in range(1, C-1, 1):
            if board[0][c] == "O":
                queue.append((0,c))
            if board[R-1][c] == "O":
                queue.append((R-1,c))


        while queue:
            r,c = queue.popleft()
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != "O":
                continue

            board[r][c] = "#"
            queue.append((r+1,c))
            queue.append((r-1,c))
            queue.append((r,c+1))
            queue.append((r,c-1))

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
    
