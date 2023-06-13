class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(grid[i])):
                col = []
                for k in range(len(grid)):
                    col.append(grid[k][j])
                if row == col:
                    count += 1
        return count