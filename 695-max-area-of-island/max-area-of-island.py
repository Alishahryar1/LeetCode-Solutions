class Solution(object):
    def helper(self, r, c, rows, cols, grid):
        if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        connected = 0
        connected += self.helper(r + 1, c, rows, cols, grid)
        connected += self.helper(r - 1, c, rows, cols, grid)
        connected += self.helper(r, c + 1, rows, cols, grid)
        connected += self.helper(r, c - 1, rows, cols, grid)
        return connected + 1

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.helper(r, c, rows, cols, grid))
        return max_area