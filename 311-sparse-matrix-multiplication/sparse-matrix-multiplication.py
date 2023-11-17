class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(mat1[0]) != len(mat2):
            return None 
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat1[0])):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res