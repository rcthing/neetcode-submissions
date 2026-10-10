class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        u, d = 0, len(matrix) - 1
        row = -1

        while u < d:
            m = (u + d) // 2
            if matrix[m][l] <= target <= matrix[m][r]:
                row = m
                break
            elif target > matrix[m][r]:
                u = m + 1
            else:
                d = m - 1
        
        if row == -1:
            row = u
            if not matrix[row][l] <= target <= matrix[row][r]:
                return False
        
        while l < r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        if matrix[row][l] != target:
            return False
        return True
