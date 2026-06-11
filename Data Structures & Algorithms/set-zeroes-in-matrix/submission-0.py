class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        if not R:
            return
        C = len(matrix[0])

        row_z = False
        col_z = False
        for c in range(C):
            if not matrix[0][c]:
                row_z = True
                break
        for r in range(R):
            if not matrix[r][0]:
                col_z = True
                break

        for r in range(1, R, 1):
            for c in range(1, C, 1):
                if not matrix[r][c]:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, R, 1):
            for c in range(1, C, 1):
                if not matrix[r][0] or not matrix[0][c]:
                    matrix[r][c] = 0

        if row_z:
            for c in range(C):
                matrix[0][c] = 0

        if col_z:
            for r in range(R):
                matrix[r][0] = 0
