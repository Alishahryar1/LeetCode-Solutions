class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L = 0
        R = len(matrix) - 1
        while (L < R):
            m = (L + R)//2
            if target > matrix[m][0]:
                if target <= matrix[m][-1]:
                    L = m
                    break
                else:
                    L = m + 1
            elif target < matrix[m][0]:
                R = m - 1
            else:
                return True
        j = L
        L = 0
        R = len(matrix[j]) - 1
        while (L <= R):
            m = (L + R)//2
            if target > matrix[j][m]:
                L = m + 1
            elif target < matrix[j][m]:
                R = m - 1
            else:
                return True
        
        return False