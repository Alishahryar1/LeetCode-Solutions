class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * cols
        for r in range(rows):
            curr_row = [0] * cols
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0
                elif c == 0 and r == 0:
                    curr_row[c] = 1
                elif c == 0:
                    curr_row[c] = prev_row[c]
                else:
                    curr_row[c] = curr_row[c - 1] + prev_row[c]
            prev_row = curr_row
        
        return curr_row[-1]
        