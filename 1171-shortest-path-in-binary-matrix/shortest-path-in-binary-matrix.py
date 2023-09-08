class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1 
        queue = deque()
        queue.append((0, 0, 1))
        grid[0][0] = 1
        length = 1
        while queue:
            r, c, length = queue.popleft()
            if r == n - 1 and c == n - 1:
                return length
            neighbours = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
            for dr, dc in neighbours:
                r_new = r + dr
                c_new = c + dc
                if min(r_new, c_new) < 0 or r_new == n or c_new == n or grid[r_new][c_new] == 1:
                    continue
                queue.append((r_new, c_new, length + 1))
                grid[r_new][c_new] = 1

        return -1