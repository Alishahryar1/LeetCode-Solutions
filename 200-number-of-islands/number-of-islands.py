class Solution(object):
    def visit(self, r, c, grid, rows, cols):
        if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.visit(r + 1, c, grid, rows, cols)
        self.visit(r - 1, c, grid, rows, cols)
        self.visit(r, c + 1, grid, rows, cols)
        self.visit(r, c - 1, grid, rows, cols)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    self.visit(r, c, grid, rows, cols)

        return islands