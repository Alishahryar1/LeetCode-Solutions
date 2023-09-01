# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = 0
        R = n
        while (L <= R):
            m = (L + R)//2
            g = guess(m)
            if g > 0:
                L = m + 1
            elif g < 0:
                R = m - 1
            else:
                return m