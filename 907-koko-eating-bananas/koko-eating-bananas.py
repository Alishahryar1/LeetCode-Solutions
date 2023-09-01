class Solution(object):
    def ceil(self, a, b):
        return int(-1 * a // b * -1)

    def canFinish(self, k, h, piles):
        if k == 0:
            return False
        
        total_h = 0
        for pile in piles:
            total_h += self.ceil(pile, k)
        
        return total_h <= h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        L = 1
        R = max(piles)
        while L <= R:
            m = (L + R)//2
            g = [self.canFinish(m - 1, h, piles), self.canFinish(m, h, piles), self.canFinish(m, h, piles)]
            if g in [[False, False, False], [False, False, True]]:
                L = m + 1
            elif g == [True, True, True]:
                R = m - 1
            else:
                return m