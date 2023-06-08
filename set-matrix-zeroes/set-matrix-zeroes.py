class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zero_pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_pos.append((i, j))
        
        for i, j in zero_pos:
            for k in range(len(matrix[i])):
                matrix[i][k] = 0
            for k in range(len(matrix)):
                matrix[k][j] = 0