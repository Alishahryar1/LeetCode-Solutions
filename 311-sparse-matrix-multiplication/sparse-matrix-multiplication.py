class Solution(object):
    def multiply(self, mat1, mat2):
        """
        :type mat1: List[List[int]]
        :type mat2: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n, o = len(mat1), len(mat2[0]), len(mat1[0])
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(m):
            for j in range(n):
                for k in range(o):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        return res