class Solution(object):
    def helper(self, text1, text2, i, j, grid):
        if i == len(text1) or j == len(text2):
            return 0
        if grid[i][j] >= 0:
            return grid[i][j]
        if text1[i] == text2[j]:
            grid[i][j] = 1 + self.helper(text1, text2, i + 1, j + 1, grid)
        else:
            grid[i][j] = max(self.helper(text1, text2, i, j + 1, grid), self.helper(text1, text2, i + 1, j, grid))
        return grid[i][j]
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        grid = [[-1] * len(text2) for _ in range(len(text1))]
        return self.helper(text1, text2, 0, 0, grid)