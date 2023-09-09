class Solution(object):
    def helper(self, coins, amount, cache):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        if amount in cache:
            return cache[amount]
        
        cache[amount] = float('inf')
        for coin in coins:
            cache[amount] = min(cache[amount], self.helper(coins, amount - coin, cache))
        cache[amount] += 1
        return cache[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ans = self.helper(coins, amount, {})
        if ans < float('inf'):
            return ans
        else:
            return -1