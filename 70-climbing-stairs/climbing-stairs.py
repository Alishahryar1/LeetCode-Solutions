class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        i = 3
        dp = [1, 2]
        while (i <= n):
            dp[0], dp[1] = dp[1], dp[0] + dp[1]
            i += 1
        return dp[-1]