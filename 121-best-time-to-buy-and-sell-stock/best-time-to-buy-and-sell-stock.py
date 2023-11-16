class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L, R = 0, 1
        profit = 0
        while (R < len(prices)):
            if prices[R] <= prices[L]:
                L = R
            profit = max(profit, prices[R] - prices[L])
            R += 1
        return profit