class Solution(object):
    def canFinish(self, k, h, piles):
        total_h = 0
        for pile in piles:
            total_h += math.ceil(pile/float(k))
        return total_h <= h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        L = 1
        R = max(piles)
        min_k = R
        while L <= R:
            m = (L + R)//2
            canFinish = self.canFinish(m, h, piles)
            if canFinish:
                min_k = min(min_k, m)
                R = m - 1
            else:
                L = m + 1
        return min_k