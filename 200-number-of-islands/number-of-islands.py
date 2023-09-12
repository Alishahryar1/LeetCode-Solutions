class Solution(object):
    def visit(self, r, c, grid, rows, cols, neighbors):
        if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0":
            return
        grid[r][c] = "0"

        for dr, dc in neighbors:
            self.visit(r + dr, c + dc, grid, rows, cols, neighbors)
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0
        neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    self.visit(r, c, grid, rows, cols, neighbors)

        return islands