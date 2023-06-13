class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_binary = bin(n)[2:]
        return n_binary.count('1')