class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        if fresh_oranges == 0:
            return 0
            
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in neighbours:
                    r_new, c_new = r + dr, c + dc
                    if min(r_new, c_new) < 0 or r_new == rows or c_new == cols or grid[r_new][c_new] in [0, 2]:
                        continue
                    fresh_oranges -= 1
                    queue.append((r_new, c_new))
                    grid[r_new][c_new] = 2
            time += 1
        if fresh_oranges == 0:
            return time
        else:
            return -1