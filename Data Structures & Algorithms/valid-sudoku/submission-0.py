class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = int(board[r][c]) # NOT NECESSARY
                if r in rows[val]:
                    return False
                else:
                    rows[val].add(r)

                if c in cols[val]:
                    return False
                else:
                    cols[val].add(c)
                
                box = 3 * (r // 3) + c // 3
                if box in boxs[val]:
                    return False
                else:
                    boxs[val].add(box)

        return True
        