class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        for coin in range(1, amount + 1):
            dp[coin] = amount + 1
            for c in coins:
                if coin - c >= 0:
                    dp[coin] = min(dp[coin], dp[coin - c])
            dp[coin] += 1
        
        if dp[-1] <= amount:
            return dp[-1]
        else:
            return -1
        