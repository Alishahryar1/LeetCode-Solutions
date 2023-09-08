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
        queue.append((0, 0))
        grid[0][0] = 1
        length = 1
        neighbours = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return length
                for dr, dc in neighbours:
                    r1, c1 = r + dr, c + dc
                    if min(r1, c1) < 0 or r1 == n or c1 == n or grid[r1][c1] == 1:
                        continue
                    queue.append((r1, c1))
                    grid[r1][c1] = 1
            length += 1 
        
        return -1