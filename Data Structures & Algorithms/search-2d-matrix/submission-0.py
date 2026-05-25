class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        # if n == 0:
        #     return False # ??
        
        mn = m * n
        l = 0
        r = mn - 1
        while l <= r:
            mid = l + (r-l) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            elif matrix[row][col] > target:
                r = mid - 1

        return False

        