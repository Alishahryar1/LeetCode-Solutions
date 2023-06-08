class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """

        for b in range(2, n - 1):
            binary = ''
            current = n
            while current > 0:

                binary = str(current % b) + binary
                current = current // b
            if binary != binary [::-1]:
                return False
        return True