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
        while (L <= R):
            m = (L + R)//2
            g = [isBadVersion(m - 1),isBadVersion(m),isBadVersion(m + 1)]
            if g == [True, True, True]:
                R = m - 1
            elif g == [False, False, False] or g == [False, False, True]:
                L = m + 1
            else:
                return m