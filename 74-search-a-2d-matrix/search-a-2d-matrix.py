class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L, R = 0, len(matrix) - 1
        while (L <= R):
            m = (L + R)//2
            if target < matrix[m][0]:
                R = m - 1
            elif target > matrix[m][-1]:
                L = m + 1
            else:
                break
        
        r, L, R = m, 0, len(matrix[m]) - 1
        while (L <= R):
            m = (L + R)//2
            if target < matrix[r][m]:
                R = m - 1
            elif target > matrix[r][m]:
                L = m + 1
            else:
                return True
        
        return False