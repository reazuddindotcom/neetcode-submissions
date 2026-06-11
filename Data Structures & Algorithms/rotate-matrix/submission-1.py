class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Q Do I have to do it in place?
        N = len(matrix)
        if not N or N != len(matrix[0]):
            return None

        l = 0
        r = N-1
        while l < r:
            for i in range(r-l):
                t, b = l, r
                tmp = matrix[t][l+i]
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][r-i]
                matrix[b][r-i] = matrix[t+i][r]
                matrix[t+i][r] = tmp

            l += 1
            r -= 1
