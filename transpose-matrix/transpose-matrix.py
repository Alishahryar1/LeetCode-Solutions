class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        matrix_t = []
        for i in range(n):
            matrix_t.append([0] * m)    
        for i in range(n):
            for j in range(m):
                matrix_t[i][j] = matrix[j][i]
        
        return matrix_t