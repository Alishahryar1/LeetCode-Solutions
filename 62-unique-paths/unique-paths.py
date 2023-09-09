class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prev_row = [0] * n
        for _ in range(m):
            curr_row = [1] * n
            for c in range(1, n):
                curr_row[c] = curr_row[c - 1] + prev_row[c]
            prev_row = curr_row
        return curr_row[-1]