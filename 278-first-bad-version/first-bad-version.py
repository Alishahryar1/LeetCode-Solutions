# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 1
        R = n
        min_v = float('inf')
        while (L <= R):
            m = (L + R)//2
            g = isBadVersion(m)
            if g:
                min_v = min(min_v, m)
                R = m - 1
            else:
                L = m + 1
        return min_v